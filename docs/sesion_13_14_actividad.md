# Sesiones 13–14 — Revisión del estado del proyecto


## 1. Proyecto y versión revisada


- **Proyecto:** P03 — Sistema de inscripciones a talleres.
- **Integrantes:** Ismael Diaz, Marcos Dominguez y Katrina Leigue.
- **Fecha:** 14 de octubre de 2026.
- **Repositorio revisado:** [katcker707/Inscripcion-Talleres](https://github.com/katcker707/Inscripcion-Talleres).
- **Rama:** `main`.
- **Commit:** [`320892eb6dd6074290f23a16e2b7fa3615024b86`](https://github.com/katcker707/Inscripcion-Talleres/tree/320892eb6dd6074290f23a16e2b7fa3615024b86).
- **Operación:** Inscripción en un taller de cupo 2, repetición de una solicitud activa y solicitud de una tercera persona cuando no quedan plazas.
**Evidencias anteriores de la versión revisada:**
- [Requisitos — sesión 6](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/docs/sesion_06_requisitos.md).
- [Historia, caso de uso y modelo — sesión 7](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/docs/sesion_07_modelos.md).
- [Plan — sesiones 8–9](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/docs/sesion-08-09-plan.md).
- [Arquitectura — sesión 12](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/docs/sesion-12-arquitectura.md).
- [Pruebas existentes](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/tests/test_reglas.py) y [README](https://github.com/katcker707/Inscripcion-Talleres/blob/320892eb6dd6074290f23a16e2b7fa3615024b86/README.md).
- [Actions de este mismo commit: ejecución 38509190386](https://github.com/katcker707/Inscripcion-Talleres/actions/runs/38509190386), rama `main`, estado `completed`, resultado `success`, comprobados mediante la API de GitHub.


Los archivos de requisitos y modelos usan guiones bajos en sus nombres. Están presentes con esas rutas, aunque la guía los ejemplifique con guiones. La revisión se refiere al código integrado en este commit; una copia independiente con cambios posteriores no acredita automáticamente su integración.


## 2. Diagnóstico
| Punto # | Estado | Evidencia concreta | Hallazgo: qué está bien o qué falta |
|---|---|---|---|
| 1. Requisitos | R | `docs/sesion_06_requisitos.md`: `TAL-RF-01`, `TAL-RF-02`, `TAL-RF-03` y pendientes; `docs/sesion_07_modelos.md`: encabezado y apartado 3 | Hay IDs y resultados comprobables|
| 2. Flujo | R | `docs/sesion_07_modelos.md`: `TAL-CU-01`, E1 y tabla de estados; `docs/sesion-12-arquitectura.md`: apartados 1 y 4 | El modelo describe espera y promoción, mientras el código confirma o rechaza por cupo; el participante solicita al operador, pero el actor del caso de uso figura como participante y debe aclararse quién interactúa con el sistema. |
| 3. Plan | P | `https://github.com/users/marcosedominguez-cyber/projects/1/views/4`: tareas A–D y apartado 7; `talleres/models.py`: fechas de inicio/fin; sesión 12, apartado 8 | El plan conserva responsables y riesgos útiles, pero su estado debe actualizarse: ya existen horarios y CI, aunque B y C siguen sin acreditar espera/promoción y D no puede considerarse terminado. |
| 4. Responsabilidades | R | `proyecto/main.py`: `ejecutar()`; `talleres/services.py`: `inscribir_participante()`; `proyecto/reglas_inscripciones.py`: función del mismo nombre | Menú y servicio están separados, pero duplicado y cupo se deciden en dos implementaciones distintas; los tests en memoria no llaman a la operación usada por el menú. |
| 5. Estilo arquitectónico | C | Sesión 12, apartados 2, 4 y 5; `proyecto/main.py`, `talleres/services.py`, `talleres/models.py` | Está documentada e implementada una separación lógica entre interacción por terminal, servicio y modelos; el compromiso es facilitar pruebas aisladas manteniendo por ahora validaciones duplicadas. No se requieren tres computadoras ni una interfaz MVC para explicar este diseño. |
| 6. Entidades y datos | P | `talleres/models.py`: `Participante`, `Taller`, `Inscripcion`, `Contador`; `talleres/migrations/0001_initial.py`; sesión 7, apartado 4 | Hay IDs internos, códigos únicos y relaciones, pero el esquema solo define `confirmada`; faltan espera/cancelación y la unicidad permanente participante/taller debe revisarse para conservar historial y permitir reinscripción. Aplicación real de índices y persistencia: No verificado en esta revisión. |
| 7. Clases y relaciones | P | `proyecto/reglas_talleres.py`: `Talleres`, `GestorTalleres`; `proyecto/reglas_inscripciones.py`: `Inscripcion`, `TallerRegistrable`; `talleres/models.py`: claves foráneas | Las responsabilidades básicas son claras: cada inscripción pertenece a un participante y a un taller, y cada uno puede tener varias inscripciones; está pendiente el armar un diagrama específico de clases/multiplicidades|
| 8. Interfaz y secuencia | P | Sesión 12, apartado 3; `proyecto/main.py`: opción 4; `talleres/services.py`: `_transaccion`, `inscribir_participante()`; reglas en memoria | El menú entrega códigos al servicio y recibe resultado/error; ambas implementaciones comprueban duplicado antes del cupo. La función en memoria válida antes de agregar; el servicio incrementa `revision` dentro de una transacción antes de validar, usando el CI. Falta diagrama de secuencia específico. |
| 9. Pruebas y CI | P | `tests/test_reglas.py`; `.github/workflows/ci-sesion12.yml`; Actions `38509190386`, SHA `320892e…`; `tests/verificar_atlas.py` | Hay 19 funciones de prueba y CI aprobado para los tres tests seleccionados de aceptación, duplicado y último cupo|
| 10. Documentación y comprensión | P | `README.md`: preparación, uso y verificación; sesión 12, apartados 5 y 8 | El README explica ejecución en PowerShell y límites, y la decisión incluye alternativas; faltan instrucciones equivalentes para Mac/Linux y comprobar que los integrantes compartan su avance para el entendimiento de todo el proyecto en conjunto.|


**Detalle de entidades y alcance:** Las clases `Talleres` y `GestorTalleres` trabajan en memoria; el modelo persistente `Taller` incorpora inicio, fin y código. No son la misma implementación. La herencia de los modelos desde `models.Model` aporta comportamiento del ORM; no se usa para conectar participante con taller, relación representada mediante `Inscripcion`. El límite de cupos cuenta confirmadas, no todos los registros históricos o en espera.


## 3. Caso crítico


**Requisitos relacionados:** `TAL-RF-03` para admitir espera o rechazar por su límite; `TAL-RF-02` como antecedente que deja pendiente el tratamiento de duplicados activos. `TAL-RF-01` exige conservar el cupo al promover, pero este recorrido no comprueba una promoción.


**Situación inicial:** taller T-01 con cupo 2, P-01 y P-02 confirmados. P-02 repite su solicitud y después P-03 pide plaza. Los códigos son los del ejemplo de la guía; en el menú se usan formatos como `P-001` y `T-001`.


| Paso | Recorrido leído en el código | Efecto deducido y límite de evidencia |
|---|---|---|
| 1. P-02 repite | Menú, opción 4 → `services.inscribir_participante()` → consulta participante/taller → comprueba duplicado antes de cupo | Lanza `InscripcionDuplicadaError` antes de crear otra inscripción. La regla en memoria sigue ese mismo orden y no modifica la lista. En Atlas, la conservación de `revision` depende del rollback transaccional no verificado aquí. |
| 2. P-03 solicita | No se encuentra duplicado → `cupos_disponibles()` devuelve 0 → rechazo | Lanza `CupoAgotadoError`; no crea un tercer registro confirmado. El código aún no consulta ni admite una lista de espera . |
| 3. Estado final | La regla en memoria solo agrega después de superar ambas validaciones | Por lectura, permanecen las dos confirmaciones originales y disponibilidad 0. No se ejecutó este escenario completo ni se comprobó el estado final real de Atlas. |


**Resultado esperado:** Conservar la inscripción de P-02, evitar otra plaza ocupada y mantener exactamente dos confirmados. La solicitud de P-03 debe recibir la espera o rechazo que determine la política acordada. Rechazar una repetición es el comportamiento actual; falta confirmar si el cliente desea ese error o devolver la inscripción existente sin error.
**Correspondencia correcta:** Tanto las reglas como el servicio detectan el duplicado antes de consultar capacidad; así, la repetición de P-02 no se confunde con una solicitud nueva a un taller lleno. En memoria, los rechazos ocurren antes del `append`.
**Pruebas disponibles:** `test_rechaza_inscripcion_duplicada_sin_ocupar_otro_cupo`, `test_rechaza_inscripcion_sin_cupo_y_no_modifica_el_estado` y `test_taller_lleno_no_tiene_cupo` aportan comprobaciones relacionadas. No recorren conjuntamente el escenario exacto de tres personas y cupo 2. El test de duplicado usa una plaza todavía libre; falta comprobar además duplicado con taller lleno y conservación completa de los registros.


**Dos fortalezas que conviene conservar:**


1. **Validación antes de agregar en memoria:** `proyecto/reglas_inscripciones.py` conserva la lista ante rechazo; los tests de duplicado y cupo agotado comprueban que no aumenta su cantidad.
2. **CI reproducible sobre una versión identificada:** el workflow selecciona tres tests existentes, genera un reporte JUnit y la ejecución `38509190386` terminó correctamente para el mismo SHA revisado. Su cobertura queda claramente limitada a reglas en memoria.


## 4. Correcciones prioritarias
Estas acciones se registran para el trabajo posterior; no se ejecutan durante esta revisión. Los responsables retoman las tareas del plan y no acreditan revisiones individuales ya realizadas.


| Prioridad | Problema | Cambio posterior | Cómo comprobaremos la corrección | Responsable / tarea del plan |
|---|---|---|---|---|
| Alta | El incremento de espera/cancelación/promoción está descrito pero falta en el código integrado; el esquema actual no conserva cancelaciones ni permite reinscripciones históricas de la misma pareja. | Implementar B según el contrato confirmado: estados, límite y orden de espera, cancelación conservada, promoción única y consulta del antecedente; adaptar la restricción de unicidad para distinguir solicitudes activas de historial. | Casos del plan con cupo 10/20: límite respetado, primera persona promovida, ocupación correcta y antecedente conservado; evidencia del mismo commit antes de cerrar D. | Marcos — B; Katrina verifica con C. |
| Alta | Las pruebas automatizadas validan otra implementación y no demuestran conservación completa ni rollback del servicio usado por el menú. | Compartir las decisiones de duplicado/cupo o comprobar explícitamente su equivalencia; ampliar pruebas del caso crítico y del adaptador, y verificar integración en una base de pruebas separada. | Tests del servicio y comparación del estado anterior/posterior, incluidos rechazo, repetición con cupo lleno y rollback de `revision`; reporte de integración y CI del commit que incorpore el cambio. | Katrina — C; Marcos apoya el adaptador; los tres — D. |


**Conclusión:** el incremento **necesita correcciones**. La inscripción básica permite continuar el trabajo y cuenta con CI aprobado de alcance limitado; no está completo el flujo de espera, cancelación y promoción. La política de espera para cupo 2 queda bloqueada hasta aclarar el redondeo. El siguiente paso es cerrar A, actualizar el estado real del plan y desarrollar B/C sin rehacer las partes que ya funcionan.


