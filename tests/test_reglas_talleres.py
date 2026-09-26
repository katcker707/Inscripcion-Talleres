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