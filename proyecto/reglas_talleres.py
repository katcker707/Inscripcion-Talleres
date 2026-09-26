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


class GestorTalleres:
    def __init__(self):
        self._talleres = {}

    def registrar_taller(self, taller: Talleres) -> None:
        if taller.id in self._talleres:
            raise ValueError("Ya existe un taller con ese identificador")

        self._talleres[taller.id] = taller

    def buscar_taller(self, id_taller: int) -> Talleres | None:
        return self._talleres.get(id_taller)