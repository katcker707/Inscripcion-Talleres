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
=================================================================== 19 passed in 0.02s ===================================================================
```
**Enlace del PR :**
https://github.com/katcker707/Inscripcion-Talleres/pull/3
(Tomar en cuenta que este PR fue el último donde se unifica los tests y se agrega otros adicionales, puesto en anteriores commits se fueron agregando otras pruebas.)
**Commit demostrado :**  [feat: agrega main.py con menu interactivo y unifica tests de reglas y añade más para verificar la funcionalidad](https://github.com/katcker707/Inscripcion-Talleres/pull/3/changes/4b9e066636f39b4daf33d617bd28a5fc73b40b9f "feat: agrega main.py con menu interactivo y unifica tests de reglas y añade más para verificar la funcionalidad")

## 8. Retroalimentación
**Decisión del equipo:**
Para mejorar la usabilidad interna de la consola antes de la demostración, el equipo decidió agregar una opción explícita en la CLI que permitiera consultar la lista de participantes registrados, facilitando la verificación de los IDs `P-XXX` generados sin necesidad de revisar las estructuras en memoria manualmente.

**Ajuste realizado:**
Se modificó `main.py` incorporando la opción de menú "6. Listar participantes registrados".

## 9. Retrospectiva

1. **Mantener:** Programación en parejas con rotación de teclado (Driver/Navigator). Ayudó a detectar inconsistencias entre las excepciones esperadas por los tests y las lanzadas en la lógica del dominio, ademas de prestar alta atencion a los pull request y mantener comunicación constante cuando estos ocurran.
    
2. **Cambiar:** La falta de consenso inicial en la nomenclatura de variables. Por ejemplo, en el módulo de talleres un integrante usó `capacidad` mientras otro usó `cupos`, lo cual generó errores al integrar. Debemos ser más detallistas al definir y ponernos de acuerdo sobre los nombres exactos de las variables antes de programar.
    
3. **Experimentar:** Diseñar una interfaz de usuario más intuitiva y accesible. Con el apoyo del docente y las observaciones de nuestros compañeros de curso, buscaremos adaptar la CLI para que sea fácil de entender y usar por cualquier tipo de persona.
    

## 10. Planificación y adaptación

- **¿Qué decisión necesitaba planificación antes de programar?**
    
    Definir con qué funcionalidad se sentía más cómodo empezando cada integrante, acotar el límite de la entrega según la capacidad que queríamos cumplir (concentrarnos en PB-01) y ponernos de acuerdo en la definición de las variables compartidas entre los distintos módulos.
    
- **¿Qué decisión pudieron mejorar gracias a una prueba o a la revisión del cliente?**
    
    Gracias a las consultas con el cliente (el docente), nos ahorramos el trabajo de desarrollar un frontend o interfaz gráfica detallada y una base de datos, además de evitar centrar esfuerzos innecesarios en la lógica de roles de usuario para esta etapa.
    
- **¿En qué contexto de su proyecto sería útil fijar más detalles por anticipado?**
    
    En el diseño de la estructura de persistencia de datos (base de datos) y la definición clara de las futuras capacidades del backlog antes de implementarlas.