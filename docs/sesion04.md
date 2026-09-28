# Iteración de la Sesión 04

## 1. Equipo y proyecto

**Proyecto:** Sistema de Inscripciones a Talleres
**Integrantes:**
* **Ismael Diaz:** Módulo de talleres, gestión de capacidad, cálculo de cupos disponibles, reglas de validacion y documentación general (`proyecto/reglas_talleres.py`, `proyecto/reglas.py`) y y documentación general (`docs/sesion04.md`).
* **Marcos Dominguez:** Módulo de participantes, registro de inscripciones, reglas de validación y documentación general(`proyecto/reglas.py` / `proyecto/reglas_usuarios.py` / `proyecto/reglas_inscripciones.py`) y documentación general (`docs/sesion04.md`).
* **Katrina Leigue:** Implementación de reglas adicionales y unificación en `proyecto/reglas.py`, interfaz interactiva de consola (`main.py`) y documentación general (`docs/sesion04.md`).

## 2. Backlog ordenado

| Orden | ID    | Capacidad                                              | ¿A quién ayuda y para qué?                                                      | Duda pendiente                                       |
| ----- | ----- | ------------------------------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 1     | PB-01 | Registrar talleres con capacidad y participantes (CLI) | Al operador, para publicar talleres con cupos límite y gestionar inscripciones. | Ninguna.                                             |
| 2     | PB-02 | Registrar participantes con ID autoincremental         | Al operador, para dar de alta personas de forma independiente.                  | Ninguna.                                             |
| 3     | PB-03 | Consultar cupos disponibles                            | Al operador, para verificar la disponibilidad antes de inscribir.               | Ninguna.                                             |
| 4     | PB-04 | Gestionar lista de espera                              | Al usuario, para quedar registrado en cola cuando el taller esté lleno.         | Política exacta de promoción (Pendiente).            |
| 5     | PB-05 | Cancelar inscripción y liberar plaza                   | Al operador, para liberar el cupo de un participante que se retira.             | ¿Se recupera la posición si re-ingresa? (Pendiente). |
| 6     | PB-06 | Emitir certificados de asistencia                      | Al participante, para acreditar su participación en el taller.                  | Formato y firma digital (Pendiente).                 |

**Razón de la primera prioridad (PB-01):** En esta entrega nos concentramos principalmente en la capacidad **PB-01** (gestión esencial de talleres con límite de capacidad e inscripciones), sentando la base de las reglas de negocio en el dominio y la consola CLI. Por otro lado, capacidades como **PB-02** y **PB-03** se integraron de forma funcional desde la interfaz (`main.py`) para permitir el flujo operativo en la consola, pero se consolidarán dentro del módulo de reglas en siguientes iteraciones. Las demás capacidades (**PB-04** a **PB-06**) quedan identificadas en el backlog pero fuera del alcance operativo de esta entrega.

## 3. Objetivo y alcance

**Objetivo de la iteración:**
Al finalizar la iteración, el operador podrá registrar participantes, crear talleres , consultar cupos e inscribir participantes mediante el menú interactivo de consola (`main.py`), garantizando que se rechacen inscripciones duplicadas y talleres sin cupo.

**Aporte consolidado:**
* **Talleres:** Creación de la clase `Talleres`, gestor de talleres e ID autoincremental (`T-001`, `T-002`, etc.).
* **Participantes:** Registro con ID autoincremental (`P-001`, `P-002`, etc.) y validación de nombre obligatorio.
* **Inscripciones y Reglas:** Verificación de existencia de participante y taller, control de cupos agotados, validaciones ampliadas en `proyecto/reglas.py` y detección de duplicados.
* **CLI (`main.py`):** Menú interactivo básico por terminal con funciones genéricas consolidadas (registrar participante/taller, inscribir, consultar cupos, ver inscripciones y listar participantes).

**Fuera del alcance de esta iteración:**
Persistencia en base de datos (MySQL/JSON), división por perfiles o roles de usuario con autenticación, cancelaciones (PB-05), promociones automáticas de lista de espera (PB-04), emisión de certificados (PB-06) e interfaz gráfica o web.


## 4. Aclaraciones del cliente

| Pregunta | Respuesta del cliente | Efecto sobre el comportamiento esperado |
| --- | --- | --- |
| ¿Hace falta que tuviera Front o solo terminal? ¿Debemos utilizar una BD? | No, no hace falta. Utilicen la memoria nomás. | Se mantiene el almacenamiento en memoria (diccionarios y listas) dentro de la CLI, omitiendo base de datos y vistas web. |
| ¿Es necesario que el script sea lo suficientemente detallado para que también verifique el usuario y muestre las funcionalidades según su perfil? | Para nada. Ese es el producto final; con que se vea una parte inicial de su proyecto es suficiente. | Se mantiene una interfaz interactiva genérica por consola sin lógica de autenticación ni separación por roles. |


## 5. Ejemplos de aceptación

| Caso | Estado inicial y entrada | Resultado esperado | Regla que lo justifica |
| --- | --- | --- | --- |
| Uso normal | Taller `T-001` con cupo 2 y participante `P-001` registrado | Inscripción confirmada y 1 cupo disponible restante. | Inscripción válida dentro del cupo permitido. |
| Límite | Taller `T-001` con cupo 1 y 1 inscripción confirmada. Entrada: `P-002` a `T-001` | Operación rechazada con `CupoAgotadoError`. Cupos disponibles: 0. | No se permite sobrepasar la capacidad asignada del taller. |
| Rechazo | Participante `P-001` ya inscrito previamente en `T-001` | Operación rechazada con `InscripcionDuplicadaError`. | Un participante solo puede inscribirse una vez por taller. |


## 6. Plan y seguimiento

| Tarea                                                               | Personas que colaboran | Estado    | Evidencia o ubicación              |
| ------------------------------------------------------------------- | ---------------------- | --------- | ---------------------------------- |
| Crear clase `Talleres`, `GestorTalleres`                            | Ismael Diaz            | Terminado | `proyecto/reglas_talleres.py`      |
| Crear clase `Participante` y funciones especificas                  | Marcos Dominguez       | Terminado | `proyecto/reglas_usuarios.py`      |
| Crear módulo de `Inscripcion` y excepciones del dominio             | Marcos Dominguez       | Terminado | `proyecto/reglas_inscripciones.py` |
| Extensión y unificación de validaciones en la lógica del negocio    | Katrina Leigue         | Terminado | `proyecto/reglas.py`               |
| Desarrollar script interactivo CLI `main.py` e integración del menú | Katrina Leigue         | Terminado | `main.py`                          |
| Unificar suite de pruebas y verificar casos bordes                  | Todo el equipo         | Terminado | `tests/test_reglas.py`             |

## 7. Verificación e integración

Se realizaron en total 19 pruebas para definir la capacidad de las funciones con diferentes casos limites.
**Resultado obtenido :**
```
