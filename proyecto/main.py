import datetime

from proyecto.reglas import (
    CupoAgotadoError,
    DatosParticipanteInvalidosError,
    InscripcionDuplicadaError,
    ParticipanteNoEncontradoError,
    TallerNoEncontradoError,
    cupos_disponibles,
    inscribir_participante,
    registrar_participante,
)
from proyecto.reglas_talleres import GestorTalleres, Talleres

def mostrar_menu():
    print("\n========================================")
    print("   SISTEMA DE GESTIÓN DE TALLERES")
    print("========================================")
    print("1. Registrar participante")
    print("2. Registrar taller")
    print("3. Listar talleres y cupos")
    print("4. Inscribir participante a un taller")
    print("5. Ver inscripciones realizadas")
    print("6. Salir")
    print("========================================")


def ejecutar():
    participantes = {}
    gestor_talleres = GestorTalleres()
    inscripciones = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        # Obtener diccionario de talleres de forma segura
        talleres_dict = getattr(
            gestor_talleres, "_talleres", getattr(gestor_talleres, "talleres", {})
        )

        if opcion == "1":
            print("\n--- REGISTRAR PARTICIPANTE ---")
            nombre = input("Nombre del participante: ").strip()
            try:
                p = registrar_participante(participantes, nombre)
                print(f" Participante registrado con éxito. ID: {p.id}")
            except DatosParticipanteInvalidosError as e:
                print(f" Error: {e}")

        elif opcion == "2":
            print("\n--- REGISTRAR TALLER ---")
            try:
                id_taller = input("ID del taller (ej. T-001): ").strip()
                nombre = input("Nombre del taller: ").strip()
                cupos = int(input("Cantidad de cupos: "))
                fecha = datetime.date.today()

                taller = Talleres(
                    id_taller=id_taller,
                    nombre=nombre,
                    cupos=cupos,
                    fecha=fecha,
                )
                gestor_talleres.registrar_taller(taller)
                print(f" Taller '{nombre}' registrado con éxito.")
            except ValueError as e:
                print(f" Error: {e}")

        elif opcion == "3":
            print("\n--- LISTA DE TALLERES ---")
            if not talleres_dict:
                print("No hay talleres registrados.")
            else:
                for t in talleres_dict.values():
                    disponibles = cupos_disponibles(t, inscripciones)
                    print(
                        f"• [{t.id}] {t.nombre} | Cupos totales: {t.cupos} | Disponibles: {disponibles}"
                    )

        elif opcion == "4":
            print("\n--- INSCRIBIR PARTICIPANTE ---")
            p_id = input("ID del participante (ej. P-001): ").strip()
            t_id = input("ID del taller (ej. T-001): ").strip()

            try:
                resultado = inscribir_participante(
                    p_id,
                    t_id,
                    participantes,
                    talleres_dict,
                    inscripciones,
                )
                print(
                    f" ¡Inscripción confirmada! Participante {resultado.participante_id} en taller {resultado.taller_id}"
                )
            except (
                ParticipanteNoEncontradoError,
                TallerNoEncontradoError,
                InscripcionDuplicadaError,
                CupoAgotadoError,
            ) as e:
                print(f" No se pudo realizar la inscripción: {e}")

        elif opcion == "5":
            print("\n--- INSCRIPCIONES REALIZADAS ---")
            if not inscripciones:
                print("Aún no hay inscripciones registradas.")
            else:
                for idx, ins in enumerate(inscripciones, start=1):
                    p_obj = participantes.get(ins.participante_id)
                    t_obj = gestor_talleres.buscar_taller(ins.taller_id)

                    p_nombre = p_obj.nombre if p_obj else ins.participante_id
                    t_nombre = t_obj.nombre if t_obj else ins.taller_id

                    print(
                        f"{idx}. {p_nombre} ({ins.participante_id}) -> {t_nombre} ({ins.taller_id}) [{ins.estado}]"
                    )

        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    ejecutar()