"""Módulo integrador que expone la API pública requerida por la guía."""

from proyecto.reglas_usuarios import (
    DatosParticipanteInvalidosError,
    Participante,
    ParticipanteError,
    registrar_participante,
)
from proyecto.reglas_inscripciones import (
    CupoAgotadoError,
    EstadoInscripcion,
    Inscripcion,
    InscripcionDuplicadaError,
    InscripcionError,
    ParticipanteNoEncontradoError,
    TallerNoEncontradoError,
    cupos_disponibles,
    inscribir_participante,
)