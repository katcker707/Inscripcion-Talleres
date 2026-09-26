import datetime


class Talleres:
    def __init__(
        self,
        id_taller: int,
        nombre: str,
        cupos: int,
        fecha: datetime.date
    ):
        self.id = id_taller
        self.nombre = nombre
        self.cupos = cupos
        self.fecha = fecha

    def calcular_cupos_disponibles(self, confirmados: int) -> int:
        return self.cupos - confirmados

    def hay_cupo(self, confirmados: int) -> bool:
        return self.calcular_cupos_disponibles(confirmados) > 0