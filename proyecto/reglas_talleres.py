import datetime


class Talleres:
    def __init__(
        self,
        nombre: str,
        cupos: int,
        fecha: datetime.date
    ):
        self.id: str | None = None
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

    def registrar_taller(self, taller: Talleres) -> Talleres:
        if taller.id is not None:
            raise ValueError("El taller ya fue registrado")

        taller.id = self._siguiente_id()
        self._talleres[taller.id] = taller
        return taller

    def buscar_taller(self, id_taller: str) -> Talleres | None:
        return self._talleres.get(id_taller)

    def _siguiente_id(self) -> str:
        numeros_existentes = [
            int(id_taller.removeprefix("T-"))
            for id_taller in self._talleres
            if id_taller.startswith("T-")
            and id_taller.removeprefix("T-").isdigit()
        ]

        siguiente_numero = max(numeros_existentes, default=0) + 1
        return f"T-{siguiente_numero:03d}"