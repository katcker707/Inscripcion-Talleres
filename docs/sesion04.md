# Iteración de la Sesión 04

## Equipo y proyecto

Proyecto: Inscripciones a talleres y listas de espera.

Integrantes:

- Ismael Diaz: talleres y capacidad.
- Pendiente: nombre del integrante responsable de participantes e inscripciones.
- Pendiente: nombre del integrante responsable de pruebas, estados e integración.

## Objetivo y alcance

El objetivo grupal de la primera iteración es permitir que un operador registre una inscripción cuando exista disponibilidad y evitar inscripciones duplicadas.

El aporte de Ismael Diaz comprende el modelo de talleres, el registro y consulta de talleres, el cálculo de cupos disponibles y la generación automática de identificadores.

Quedan fuera de este aporte las cancelaciones, la lista de espera, la base de datos y la interfaz gráfica.

## Plan y seguimiento

| Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|
| Crear la clase `Talleres` | Ismael Diaz | Terminado | `proyecto/reglas_talleres.py` |
| Generar automáticamente el ID del taller | Ismael Diaz | Terminado | IDs consecutivos `T-001`, `T-002`, etc. |
| Guardar nombre, cupos y fecha | Ismael Diaz | Terminado | `tests/test_reglas.py` |
| Calcular cupos disponibles | Ismael Diaz | Terminado | Método `calcular_cupos_disponibles()` |
| Comprobar si existe cupo | Ismael Diaz | Terminado | Método `hay_cupo()` |
| Registrar y buscar talleres | Ismael Diaz | Terminado | Clase `GestorTalleres` |
| Evitar que el usuario ingrese el identificador | Ismael Diaz | Terminado | `proyecto/main.py` |
| Integrar talleres con participantes e inscripciones | Equipo | Terminado | `tests/test_reglas.py` |

## Ajuste de identificador automático

Inicialmente, el usuario tenía que escribir manualmente el identificador del taller. Esto podía provocar identificadores repetidos o escritos incorrectamente.

Se modificó el sistema para que la clase `GestorTalleres` genere identificadores consecutivos automáticamente:

- Primer taller: `T-001`.
- Segundo taller: `T-002`.
- Tercer taller: `T-003`.

Ahora el usuario solamente introduce el nombre y la cantidad de cupos. Después del registro, el sistema muestra el identificador generado.

También se actualizaron el menú principal y las pruebas de integración para utilizar los nuevos identificadores automáticos.

## Verificación e integración

Ramas utilizadas:

- `feature/talleres-capacidad`
- `feature/id-taller-automatico`

Pruebas ejecutadas:

```bash
python -m pytest -q
```

Resultado:

```text
19 passed
```