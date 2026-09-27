from dataclasses import dataclass

import pytest

from proyecto.reglas import (
    CupoAgotadoError,
    DatosParticipanteInvalidosError,
    EstadoInscripcion,
    InscripcionDuplicadaError,
    ParticipanteNoEncontradoError,
    TallerNoEncontradoError,
    cupos_disponibles,
    inscribir_participante,
    registrar_participante,
)


@dataclass(frozen=True)
class TallerParaPruebas:
    """Contrato mínimo que implementará el módulo de talleres."""

    id: str
    capacidad: int


def test_registra_participante_con_identificador_automatico():
    participantes = {}

    resultado = registrar_participante(participantes, "Ana Pérez")

    assert resultado.id == "P-001"
    assert resultado.nombre == "Ana Pérez"
    assert participantes == {"P-001": resultado}


def test_genera_identificadores_consecutivos_sin_que_el_usuario_los_elija():
    participantes = {}

    ana = registrar_participante(participantes, "Ana Pérez")
    bruno = registrar_participante(participantes, "Bruno Díaz")

    assert ana.id == "P-001"
    assert bruno.id == "P-002"
    assert len(participantes) == 2


def test_rechaza_nombre_vacio_sin_consumir_un_identificador():
    participantes = {}

    with pytest.raises(DatosParticipanteInvalidosError, match="nombre"):
        registrar_participante(participantes, "   ")

    assert participantes == {}
    assert registrar_participante(participantes, "Ana Pérez").id == "P-001"


def test_inscribe_participante_y_confirma_la_plaza_disponible():
    participantes = {}
    participante = registrar_participante(participantes, "Ana Pérez")
    taller = TallerParaPruebas(id="T-001", capacidad=2)
    talleres = {taller.id: taller}
    inscripciones = []

    resultado = inscribir_participante(
        participante.id,
        taller.id,
        participantes,
        talleres,
        inscripciones,
    )

    assert resultado.participante_id == "P-001"
    assert resultado.taller_id == "T-001"
    assert resultado.estado == EstadoInscripcion.CONFIRMADA
    assert inscripciones == [resultado]
    assert cupos_disponibles(taller, inscripciones) == 1


def test_inscripcion_en_el_ultimo_cupo_deja_el_taller_sin_disponibilidad():
    participantes = {}
    participante = registrar_participante(participantes, "Ana Pérez")
    taller = TallerParaPruebas(id="T-001", capacidad=1)
    talleres = {taller.id: taller}
    inscripciones = []

    inscribir_participante(
        participante.id,
        taller.id,
        participantes,
        talleres,
        inscripciones,
    )

    assert cupos_disponibles(taller, inscripciones) == 0


def test_rechaza_inscripcion_duplicada_sin_ocupar_otro_cupo():
    participantes = {}
    participante = registrar_participante(participantes, "Ana Pérez")
    taller = TallerParaPruebas(id="T-001", capacidad=2)
    talleres = {taller.id: taller}
    inscripciones = []
    inscribir_participante(
        participante.id, taller.id, participantes, talleres, inscripciones
    )

    with pytest.raises(InscripcionDuplicadaError, match="ya está inscrito"):
        inscribir_participante(
            participante.id, taller.id, participantes, talleres, inscripciones
        )

    assert len(inscripciones) == 1
    assert cupos_disponibles(taller, inscripciones) == 1


def test_rechaza_inscripcion_sin_cupo_y_no_modifica_el_estado():
    participantes = {}
    ana = registrar_participante(participantes, "Ana Pérez")
    bruno = registrar_participante(participantes, "Bruno Díaz")
    taller = TallerParaPruebas(id="T-001", capacidad=1)
    talleres = {taller.id: taller}
    inscripciones = []
    inscribir_participante(
        ana.id, taller.id, participantes, talleres, inscripciones
    )

    with pytest.raises(CupoAgotadoError, match="no tiene cupos"):
        inscribir_participante(
            bruno.id, taller.id, participantes, talleres, inscripciones
        )

    assert len(inscripciones) == 1
    assert inscripciones[0].participante_id == ana.id


def test_rechaza_inscripcion_de_participante_inexistente_sin_modificar_el_estado():
    taller = TallerParaPruebas(id="T-001", capacidad=2)
    inscripciones = []

    with pytest.raises(ParticipanteNoEncontradoError, match="P-999"):
        inscribir_participante(
            "P-999", taller.id, {}, {taller.id: taller}, inscripciones
        )

    assert inscripciones == []


def test_rechaza_inscripcion_en_taller_inexistente_sin_modificar_el_estado():
    participantes = {}
    participante = registrar_participante(participantes, "Ana Pérez")
    inscripciones = []

    with pytest.raises(TallerNoEncontradoError, match="T-999"):
        inscribir_participante(
            participante.id,
            "T-999",
            participantes,
            {},
            inscripciones,
        )

    assert inscripciones == []
