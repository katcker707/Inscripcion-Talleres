
## Sesión 6 — Hallazgos y requisitos del proyecto

- **Proyecto:** Sistema de inscripciones a talleres
- **Integrantes:** Pendiente de completar por el equipo
- **Fecha:** 2026-10-01
- **Cliente o fuente consultada:**Ing. Sergio Barrientos, grabación de la entrevista, notas del equipo y guía de la actividad
- **Flujo seleccionado:** Inscripción y cancelación de participantes, con control de cupo, lista de espera y promoción automática
## 1. Hallazgos de la entrevista


| ID | Pregunta | Respuesta o hallazgo | Fuente | Estado |
|---|---|---|---|---|
| ENT-01 | ¿Qué ocurre cuando no quedan plazas? | La persona puede ingresar en la lista de espera mientras esta no haya alcanzado su límite. Si la espera también está llena, no se admite la solicitud. | Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-02 | ¿Cómo se ordena la lista de espera y cómo se resuelven solicitudes simultáneas? | Se usa el orden de inscripción: primero en entrar, primero en ser atendido. Las notas indican que se ordena por fecha y hora (`datetime`)| Cliente (Ing. Sergio Barrientos) | Confirmado|
| ENT-03 | ¿Quién recibe una plaza liberada? | La primera persona de la lista de espera pasa automáticamente a confirmada y recibe una notificación de que quedó inscrita. No se solicita una aceptación adicional. | Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-04 | ¿Qué sucede si una persona vuelve a solicitar el mismo taller? | Después de cancelar puede inscribirse nuevamente como una solicitud nueva. Si el taller está lleno, queda al final de la lista de espera y no recupera su posición anterior.| Cliente (Ing. Sergio Barrientos) | Confirmado 
| ENT-05 | ¿Qué identifica de manera única a una persona? | A la hora de autenticar al usuario (participante), se le pedirá un id global, por ejemplo: su cédula de identidad| Cliente (Ing. Sergio Barrientos) | Pendiente|
| ENT-06 | ¿Cuándo abre y cierra la inscripción? | Se permite inscribirse hasta un minuto antes del inicio. Una vez iniciado el taller no se aceptan inscripciones, sin importar su duración, por ahora. No se indicó cuándo se abre la inscripción. | Cliente (Ing. Sergio Barrientos) |Confirmado|
| ENT-07 | ¿Una persona que cancela conserva su posición o su historial? | No conserva la posición. La cancelación debe quedar registrada y visible en el perfil; una re-inscripción posterior no elimina ese antecedente. | Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-08 | ¿Qué ocurre si aumenta o disminuye el cupo? | En la grabación se planteó que un aumento podría promover personas de la espera,se decidió revocarle los cupos a los últimos inscritos | Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-09 | ¿Se permiten inscripciones en talleres con horarios superpuestos? | No. Una misma persona no puede quedar inscrita en dos talleres que ocurran al mismo tiempo. | Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-10 | ¿Cuál es la interacción entre participante y operador? | El participante se comunicará con el operador dependiendo del taller de su interés, el operador será el encargado de inscribir al participante en el sistema.| Cliente (Ing. Sergio Barrientos) | Confirmado |
| ENT-11 | ¿Cuál es el límite de la lista de espera? | La lista de espera admite como máximo el 20 % del cupo del taller. |Cliente (Ing. Sergio Barrientos) | Confirmado|
| ENT-12 | ¿Hasta cuándo puede cancelarse sin penalización? | La persona puede cancelar sin quedar marcada como penalizada hasta tres horas antes del inicio del taller. | Cliente (Ing. Sergio Barrientos) | Confirmada|
| ENT-13 | ¿Qué ocurre si llega la hora de inicio y no hay participantes? | Se indicó que el taller se cancela automáticamente si no tiene participantes.  | Cliente (Ing. Sergio Barrientos)| Confirmada |


## 2. Alcance del flujo


### Incluye


- Solicitar una inscripción antes del límite temporal.
- Confirmar la inscripción cuando exista cupo.
- Incorporar a la persona en una lista de espera ordenada cuando el cupo está completo.
- Limitar la espera al 20 % del cupo del taller.
- Promover automáticamente a la primera persona en espera cuando se libera una plaza.
- Notificar a la persona promovida que quedó inscrita.
- Reinscribir como solicitud nueva a quien había cancelado.
- Impedir que una misma persona se inscriba en talleres con horarios superpuestos.


### No incluye 
- Creación, publicación y edición de talleres por el coordinador.
- Definición final del identificador global de participante.
- Flujo detallado y permisos de participante, operador, coordinador e instructor.
- Penalizaciones por cancelación tardía, inasistencia o inscripciones abusivas.
- Implementación, interfaz, persistencia y pruebas ejecutadas.


## 3. Requisitos


### TAL-RF-01 — Promoción automática por orden de espera


- **Tipo:** Funcional
- **Origen:** ENT-02 y ENT-03; entrevista con el cliente. Adapta el escenario `TAL-RF-02` de la guía únicamente en lo confirmado por el cliente.
- **Prioridad y razón:** Alta, porque determina quién obtiene una plaza liberada y evita asignaciones arbitrarias.
- **Estado:** Aprobado por el cliente. El desempate de solicitudes con marcas de tiempo idénticas sigue pendiente.
- **Requisito:** Cuando se libera una plaza antes del inicio y existe una lista de espera, el sistema debe confirmar automáticamente a la persona que ocupa la primera posición, mantener el orden de las demás y notificar a la persona promovida, sin superar el cupo del taller.
- **Criterio de aceptación:**
  - **Situación inicial:** El taller T-01 tiene cupo 2; A y B están confirmados; C y D están en espera, en ese orden.
  - **Acción:** A cancela antes del inicio.
  - **Resultado esperado:** C queda confirmada automáticamente y recibe una notificación de inscripción; D continúa en espera; el taller conserva 2 plazas ocupadas; la cancelación de A permanece registrada.


### TAL-RF-02 — Reinscripción después de cancelar


- **Tipo:** Funcional
- **Origen:** ENT-04 y ENT-07; entrevista con el cliente.
- **Prioridad y razón:** Alta, porque protege el orden de la espera y conserva la trazabilidad de cancelaciones.
- **Estado:** Aprobado por el cliente para el caso posterior a una cancelación. El tratamiento de un envío duplicado mientras existe una inscripción activa sigue pendiente.
- **Requisito:** Cuando una persona que canceló solicita nuevamente el mismo taller, el sistema debe tratar la solicitud como una inscripción nueva. Si hay una plaza disponible, puede confirmarla; si el cupo está completo y la espera admite otra persona, debe colocarla al final de la lista sin recuperar su posición anterior. El antecedente de cancelación debe permanecer visible en su perfil.
- **Criterio de aceptación:**
  - **Situación inicial:** P-01 canceló su inscripción en T-01; el taller está completo y C y D forman la lista de espera, en ese orden.
  - **Acción:** P-01 solicita inscribirse otra vez y la lista de espera aún tiene capacidad.
  - **Resultado esperado:** P-01 queda después de D en la lista de espera; no desplaza a C ni a D; la cancelación anterior continúa visible en su perfil.


### TAL-RF-03 — Límite de la lista de espera


- **Tipo:** Funcional
- **Origen:** ENT-01 y ENT-11; entrevista con el cliente.
- **Prioridad y razón:** Alta, porque define cuándo una solicitud puede incorporarse a la espera y cuándo debe rechazarse.
- **Estado:** Aprobado por el cliente para cupos cuyo 20 % es entero. El método de redondeo para otros cupos está pendiente.
- **Requisito:** Cuando el taller está completo, el sistema debe admitir solicitudes en la lista de espera solo hasta alcanzar el 20 % del cupo máximo. Al alcanzar ese límite debe rechazar nuevas solicitudes de espera y no modificar el orden ni los registros existentes.
- **Criterio de aceptación:**
  - **Situación inicial:** T-01 tiene cupo 20, sus 20 plazas están ocupadas y hay 4 personas en espera.
  - **Acción:** P-25 solicita inscribirse.
  - **Resultado esperado:** La solicitud no se incorpora a la lista; la espera conserva exactamente 4 personas en el mismo orden; las 20 inscripciones confirmadas no cambian; el sistema informa que la lista de espera está completa.


### TAL-RF-04 — Rechazo por superposición horaria


- **Tipo:** Funcional
- **Origen:** ENT-09; entrevista con el cliente.
- **Prioridad y razón:** Alta, porque evita confirmar la asistencia de una persona a dos talleres simultáneos.
- **Estado:** Aprobado por el cliente para horarios que se solapan. El tratamiento de horarios adyacentes está pendiente.
- **Requisito:** Si una persona ya tiene una inscripción confirmada en un taller y solicita otro cuyo horario se superpone, el sistema debe rechazar la nueva inscripción, no crear un segundo registro activo y conservar sin cambios la inscripción previa.
- **Criterio de aceptación:**
  - **Situación inicial:** P-01 está confirmada en T-01 de 10:00 a 12:00; T-02 ocurre de 11:00 a 13:00 y tiene cupo disponible.
  - **Acción:** P-01 solicita inscribirse en T-02.
  - **Resultado esperado:** La solicitud a T-02 se rechaza por superposición; P-01 conserva su inscripción en T-01; no se ocupa una plaza de T-02.


### TAL-RC-01 — Trazabilidad visible de cancelaciones


- **Tipo:** Calidad — trazabilidad e integridad de la información
- **Origen:** ENT-07; TXT y grabación.
- **Prioridad y razón:** Alta, porque el historial permite distinguir una re-inscripción nueva de una inscripción nunca cancelada y podrá sustentar reglas futuras ante usos abusivos.
- **Estado:** Aprobado por el cliente en cuanto a conservar y mostrar la cancelación. Los campos exactos del historial están pendientes.
- **Requisito:** El sistema debe conservar el antecedente de cada inscripción cancelada y mantenerlo visible en el perfil del participante aunque posteriormente se inscriba de nuevo, sin reemplazarlo por el nuevo estado.
- **Criterio de aceptación o comprobación:**
  - **Situación inicial:** P-01 tiene una inscripción cancelada en T-01.
  - **Acción:** P-01 vuelve a solicitar T-01 y obtiene una nueva inscripción.
  - **Resultado esperado:** El perfil permite observar tanto el antecedente cancelado como la nueva solicitud; la re-inscripción no borra ni convierte el registro anterior en activo.


### TAL-RT-01 — Cierre temporal de inscripciones


- **Tipo:** Restricción de negocio
- **Origen:** ENT-06; TXT y grabación.
- **Prioridad y razón:** Alta, porque establece el instante máximo en que el sistema puede aceptar participantes.
- **Estado:** Aprobado por el cliente para la versión actual.
- **Restricción:** Una inscripción solo puede registrarse hasta un minuto antes de la hora de inicio del taller. A la hora de inicio o después, el sistema debe impedir cualquier inscripción, aunque existan plazas y aunque el taller dure más de un día.
- **Criterio de comprobación:**
  - **Situación inicial:** T-01 comienza a las 12:00 y tiene plazas disponibles.
  - **Acción:** P-01 solicita una plaza a las 11:59 y P-02 la solicita a las 12:00.
  - **Resultado esperado:** La solicitud de P-01 puede continuar si cumple las demás reglas; la de P-02 se rechaza por haber comenzado el taller y no ocupa una plaza.


## 4. Escenarios del flujo


| Caso | Requisito relacionado | Datos y acción | Resultado esperado |
|---|---|---|---|
| Normal | TAL-RF-01 | Cupo 2; A y B confirmados; C y D en espera. A cancela antes del inicio. | C queda confirmada automáticamente y notificada; D conserva su posición; la ocupación sigue en 2 y la cancelación de A queda registrada. |
| Límite | TAL-RT-01 | El taller inicia a las 12:00 y P-01 solicita la inscripción a las 11:59. | La solicitud puede aceptarse si cumple las demás reglas. A las 12:00 ya debe rechazarse. |
| Rechazo | TAL-RF-03 | Taller completo de cupo 20 y lista de espera con 4 personas; P-25 intenta ingresar. | Se rechaza la nueva solicitud por lista llena; no cambian las 20 confirmaciones ni el orden de las 4 personas en espera. |




## 5. Preguntas y decisiones pendientes


| Pregunta o decisión | A quién consultar | Impacto mientras no se resuelva |
|---|---|---|
| ¿El identificador del participante es global o depende del taller? ¿Qué formato final debe usar? | Cliente (Ing. Sergio Barrientos) | Afecta el modelo de datos y la detección de duplicados y superposiciones. |
| ¿Cómo se redondea el 20 % cuando el resultado no es entero? | Cliente (Ing. Sergio Barrientos) | Afecta TAL-RF-03 para cupos como 12 o 15. |
| ¿Qué consecuencia concreta tiene cancelar con menos de tres horas o no asistir? | Cliente (Ing. Sergio Barrientos) | No puede implementarse todavía una política de penalización o detección de abuso. |
| ¿Qué canal se usa para las notificaciones y qué ocurre si la entrega falla? | Cliente (Ing. Sergio Barrientos) | Afecta el detalle de TAL-RF-01 y la cancelación automática del taller. |
| ¿En qué instante se cancela un taller sin participantes y a quién se notifica? | Cliente (Ing. Sergio Barrientos) | La regla general está confirmada, pero no es todavía un requisito completamente verificable. |


## 6. Participación y asistencia utilizada


- **Aportes de cada integrante:**
 - **Ismael Diaz:** Formulación de preguntas sobre la lista de espera y cancelaciones.
 - **Marcos Dominguez:** Redacción de escenarios del flujo y límites de tiempo.
 - **Katrina Leigue:** Redacción de los requisitos de usuario autenticado, revisión del archivo y actualización del repositorio en GitHub.
- **Asistencia de IA, si se utilizó:** ChatGPT / Gemini para estructurar el formato del Markdown según la plantilla requerida.

