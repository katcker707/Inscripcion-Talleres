import datetime

import pytest

from proyecto.reglas_talleres import GestorTalleres, Talleres


def test_crear_taller_guarda_sus_datos():
    taller = Talleres(
        id_taller=1,
        nombre="Python básico",
        cupos=20,
        fecha=datetime.date(2026, 10, 15)
    )

    assert taller.id == 1
    assert taller.nombre == "Python básico"
    assert taller.cupos == 20
    assert taller.fecha == datetime.date(2026, 10, 15)


def test_calcular_cupos_disponibles():
    taller = Talleres(
        id_taller=2,
        nombre="Diseño gráfico",
        cupos=5,
        fecha=datetime.date(2026, 11, 10)
    )

    assert taller.calcular_cupos_disponibles(3) == 2


def test_taller_lleno_no_tiene_cupo():
    taller = Talleres(
        id_taller=3,
        nombre="Fotografía",
        cupos=2,
        fecha=datetime.date(2026, 12, 5)
    )

    assert taller.hay_cupo(2) is False


def test_registrar_y_buscar_taller():
    gestor = GestorTalleres()

    taller = Talleres(
        id_taller=4,
        nombre="Marketing digital",
        cupos=10,
        fecha=datetime.date(2026, 11, 20)
    )

    gestor.registrar_taller(taller)

    assert gestor.buscar_taller(4) is taller


def test_rechazar_identificador_duplicado_sin_reemplazar():
    gestor = GestorTalleres()

    taller_original = Talleres(
        id_taller=5,
        nombre="Excel básico",
        cupos=15,
        fecha=datetime.date(2026, 12, 1)
    )

    taller_duplicado = Talleres(
        id_taller=5,
        nombre="Excel avanzado",
        cupos=8,
        fecha=datetime.date(2026, 12, 2)
    )

    gestor.registrar_taller(taller_original)

    with pytest.raises(ValueError, match="Ya existe"):
        gestor.registrar_taller(taller_duplicado)

    assert gestor.buscar_taller(5) is taller_original


def test_buscar_taller_inexistente_devuelve_none():
    gestor = GestorTalleres()

    assert gestor.buscar_taller(999) is None