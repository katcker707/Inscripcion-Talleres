"""Prueba real en una base temporal. Ejecutar desde la raíz con python tests/verificar_atlas.py."""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from pathlib import Path
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
nombre_prueba = "test_cli_" + uuid4().hex[:16]
os.environ["MONGODB_DATABASE"] = nombre_prueba
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
from django.core.management import call_command
from django.core.exceptions import ValidationError
from django.db import connection, connections, IntegrityError
from django.utils import timezone
from proyecto.reglas_inscripciones import (
    CupoAgotadoError, InscripcionDuplicadaError,
    ParticipanteNoEncontradoError, TallerNoEncontradoError,
)
from proyecto.reglas_usuarios import DatosParticipanteInvalidosError
from talleres import services
from talleres.models import Participante, Taller, Inscripcion


def esperar_error(tipo, funcion, *args, **kwargs):
    try:
        funcion(*args, **kwargs)
    except tipo:
        return
    raise AssertionError(f"No se rechazó la operación con {tipo.__name__}")


def menu(entrada):
    result = subprocess.run(
        [sys.executable, "-m", "proyecto.main"], input=entrada,
        text=True, capture_output=True, timeout=60,
        encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        cwd=Path(__file__).resolve().parent.parent,
    )
    assert result.returncode == 0, result.stderr
    assert "No se pudo completar" not in result.stdout, result.stdout
    return result.stdout


try:
    assert connection.settings_dict["NAME"] == nombre_prueba
    # Reproducir las tres colecciones vacías creadas manualmente en Atlas.
    for coleccion in ("participantes", "talleres", "inscripciones"):
        connection.database.create_collection(coleccion)
    call_command("migrate", "talleres", verbosity=0, interactive=False)
    esperar_error(DatosParticipanteInvalidosError, services.registrar_participante, "   ")
    ana = services.registrar_participante("Ana prueba")
    bruno = services.registrar_participante("Bruno prueba")
    assert ana.codigo == "P-001" and bruno.codigo == "P-002"
    inicio = timezone.now() + timedelta(days=1)
    esperar_error(ValidationError, services.registrar_taller, "Inválido", 0, inicio, inicio)
    taller = services.registrar_taller("Taller prueba", 1, inicio, inicio + timedelta(hours=2))
    assert taller.codigo == "T-001"
    esperar_error(ParticipanteNoEncontradoError, services.inscribir_participante, "P-999", taller.codigo)
    esperar_error(TallerNoEncontradoError, services.inscribir_participante, ana.codigo, "T-999")
    services.inscribir_participante(ana.codigo, taller.codigo)
    esperar_error(InscripcionDuplicadaError, services.inscribir_participante, ana.codigo, taller.codigo)
    esperar_error(CupoAgotadoError, services.inscribir_participante, bruno.codigo, taller.codigo)
    assert Inscripcion.objects.count() == 1 and services.cupos_disponibles(taller) == 0
    esperar_error(IntegrityError, Inscripcion.objects.create, participante=ana, taller=taller)
    # Procesos distintos: registrar, cerrar y volver a consultar desde el menú.
    assert "P-003" in menu("1\nPersistencia CLI\n7\n")
    salida = menu("6\n3\n5\n7\n")
    assert "Persistencia CLI" in salida and "Taller prueba" in salida and "confirmada" in salida
    # Dos solicitudes simultáneas a la última plaza.
    otro = services.registrar_taller("Concurrente", 1, inicio, inicio + timedelta(days=2))
    def inscribir(codigo):
        try:
            services.inscribir_participante(codigo, otro.codigo)
            return "confirmada"
        except CupoAgotadoError:
            return "lleno"
        finally:
            connections.close_all()
    with ThreadPoolExecutor(max_workers=2) as executor:
        resultados = list(executor.map(inscribir, [ana.codigo, bruno.codigo]))
    assert sorted(resultados) == ["confirmada", "lleno"], resultados
    assert Inscripcion.objects.filter(taller=otro).count() == 1
    # Códigos generados simultáneamente, sin duplicados.
    def registrar(numero):
        try:
            return services.registrar_participante(f"Concurrente {numero}").codigo
        finally:
            connections.close_all()
    with ThreadPoolExecutor(max_workers=3) as executor:
        codigos = list(executor.map(registrar, range(3)))
    assert len(set(codigos)) == 3
    print("OK: colecciones existentes, validaciones, duplicados, cupos, concurrencia y persistencia entre procesos.")
finally:
    if connection.settings_dict["NAME"] != nombre_prueba or not nombre_prueba.startswith("test_cli_"):
        raise RuntimeError("Se impidió limpiar una base distinta de la temporal.")
    connection.database.client.drop_database(nombre_prueba)
    connections.close_all()
    print("Base temporal de prueba eliminada; talleres_db no recibió datos de prueba.")
