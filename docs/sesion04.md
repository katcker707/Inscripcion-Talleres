# Iteración de la Sesión 04

## Equipo y proyecto

Proyecto: Inscripciones a talleres y listas de espera.

Integrantes:

- Ismael Diaz: talleres y capacidad.
- Pendiente: nombre del integrante responsable de participantes e inscripciones.
- Pendiente: nombre del integrante responsable de pruebas, estados e integración.

## Objetivo y alcance

El objetivo grupal de la primera iteración es permitir que un operador registre una inscripción cuando exista disponibilidad y evitar inscripciones duplicadas.

El aporte de Ismael Diaz comprende el modelo de talleres, el registro y consulta de talleres, y el cálculo de cupos disponibles.

Quedan fuera de este aporte las inscripciones, participantes, cancelaciones, lista de espera, base de datos e interfaz gráfica.

## Plan y seguimiento

| Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|
| Crear la clase `Talleres` | Ismael Diaz | Terminado | `proyecto/reglas_talleres.py` |
| Guardar identificador, nombre, cupos y fecha | Ismael Diaz | Terminado | `tests/test_reglas_talleres.py` |
| Calcular cupos disponibles | Ismael Diaz | Terminado | Método `calcular_cupos_disponibles()` |
| Comprobar si existe cupo | Ismael Diaz | Terminado | Método `hay_cupo()` |
| Registrar y buscar talleres | Ismael Diaz | Terminado | Clase `GestorTalleres` |
| Rechazar identificadores duplicados | Ismael Diaz | Terminado | Prueba de rechazo y conservación del taller original |
| Integrar con participantes e inscripciones | Equipo | Pendiente | Trabajo posterior |

## Verificación e integración

Rama utilizada:

`feature/talleres-capacidad`

Pruebas ejecutadas:

```bash
python -m pytest -q