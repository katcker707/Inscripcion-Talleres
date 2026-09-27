"""Reglas para registrar participantes en memoria."""

from dataclasses import dataclass


class ParticipanteError(Exception):
    """Error base de las operaciones con participantes."""


class DatosParticipanteInvalidosError(ParticipanteError, ValueError):
    """Los datos del participante no cumplen las reglas mínimas."""


@dataclass(frozen=True)
class Participante:
    """Persona que puede solicitar una plaza en un taller."""

    id: str
    nombre: str

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise DatosParticipanteInvalidosError(
                "El identificador del participante es obligatorio."
            )
        if not self.nombre.strip():
            raise DatosParticipanteInvalidosError(
                "El nombre del participante es obligatorio."
            )


def registrar_participante(
    participantes: dict[str, Participante], nombre: str
) -> Participante:
    """Crea y registra un participante con un ID consecutivo automático."""

    participante = Participante(
        id=_siguiente_id(participantes),
        nombre=nombre,
    )
    participantes[participante.id] = participante
    return participante


def _siguiente_id(participantes: dict[str, Participante]) -> str:
    """Genera un ID nuevo sin reutilizar números anteriores."""

    numeros_existentes = [
        int(participante_id.removeprefix("P-"))
        for participante_id in participantes
        if participante_id.startswith("P-")
        and participante_id.removeprefix("P-").isdigit()
    ]
    siguiente_numero = max(numeros_existentes, default=0) + 1
    return f"P-{siguiente_numero:03d}"
