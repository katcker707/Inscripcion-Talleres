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