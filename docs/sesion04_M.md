# Iteración de la Sesión 04

## Equipo y proyecto

Proyecto: Inscripciones a talleres y listas de espera.

Integrantes:

- Ismael Diaz: talleres y capacidad.
- Pendiente: nombre del integrante responsable de participantes e inscripciones.
- Pendiente: nombre del integrante responsable de pruebas, estados e integración.

## Objetivo y alcance

El objetivo grupal de la primera iteración es permitir que un operador registre
una inscripción cuando exista disponibilidad y evitar inscripciones duplicadas.

El aporte correspondiente a participantes e inscripciones comprende el registro
de participantes con identificadores automáticos, la creación de inscripciones,
la validación de participantes y talleres, el control de cupos y la detección de
inscripciones duplicadas.

Quedan fuera de este aporte las cancelaciones, la lista de espera, la
persistencia en base de datos y la interfaz gráfica. Cuando un taller no tiene
cupos, la operación se rechaza provisionalmente hasta que el cliente defina si
la persona debe pasar a una lista de espera.

## Plan y seguimiento

| Tarea | Responsable | Estado | Evidencia |
| --- | --- | --- | --- |
| Crear la clase `Participante` | Participantes e inscripciones | Terminado | `proyecto/reglas_usuarios.py` |
| Generar identificadores consecutivos automáticamente | Participantes e inscripciones | Terminado | Función `_siguiente_id()` |
| Validar que el nombre sea obligatorio | Participantes e inscripciones | Terminado | `DatosParticipanteInvalidosError` |
| Crear la clase `Inscripcion` y su estado | Participantes e inscripciones | Terminado | `proyecto/reglas_inscripciones.py` |
| Verificar que participante y taller existan | Participantes e inscripciones | Terminado | Función `inscribir_participante()` |
| Evitar inscripciones duplicadas | Participantes e inscripciones | Terminado | `InscripcionDuplicadaError` y prueba de rechazo |
| Impedir inscripciones confirmadas sin cupo | Participantes e inscripciones | Terminado | `CupoAgotadoError` y prueba de último cupo |
| Crear pruebas de casos normales, límites y rechazos | Participantes e inscripciones | Terminado | `tests/test_reglas.py` |
| Integrar con la implementación definitiva de talleres | Equipo | Pendiente | Sustituir `TallerParaPruebas` por `Talleres` o adaptar el contrato |

## Aclaraciones pendientes del cliente

| Pregunta | Estado | Decisión provisional |
| --- | --- | --- |
| ¿Qué identifica de forma única a una persona? | Pendiente | El sistema genera IDs consecutivos como `P-001`. |
| ¿Qué sucede cuando se llena el taller? | Pendiente | No se crea otra inscripción confirmada. |
| ¿Puede reinscribirse alguien que canceló? | Pendiente | Cancelación y reinscripción quedan fuera de este avance. |

Estas decisiones son provisionales y no representan respuestas aprobadas por el
cliente.

## Ejemplos de aceptación

| Caso | Estado inicial y entrada | Resultado esperado |
| --- | --- | --- |
| Uso normal | Taller `T-001` con capacidad 2 y participante registrado | Inscripción confirmada y 1 cupo restante |
| Límite | Taller `T-001` con capacidad 1 y participante registrado | Inscripción confirmada y 0 cupos restantes |
| Rechazo | El participante ya está inscrito en `T-001` | La operación se rechaza y no se agrega otra inscripción |

## Verificación e integración

Rama utilizada:

`iteracion01/participantes-inscripciones`

Pruebas ejecutadas:

```bash
python -m pytest -q
```

Resultado obtenido:

```text
9 passed
```

La integración con `proyecto/reglas_talleres.py` permanece pendiente hasta que
la rama de talleres y capacidad esté disponible en la misma versión del
proyecto.
