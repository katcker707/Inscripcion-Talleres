import datetime

from proyecto.reglas_talleres import Talleres


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