# Inscripcion-Talleres
Una organización ofrece talleres con cupos limitados. Puede ser una academia, asociación profesional, organización cultural o centro de formación. Actualmente registra interesados en formularios y confirma plazas manualmente. Aparecen inscripciones duplicadas, dudas sobre quién estaba primero y lugares vacíos después de una cancelación.

## Versión de terminal con Django y MongoDB Atlas

Se conservan las siete opciones del menú. Django proporciona los modelos y el
acceso a Atlas; no hace falta iniciar un servidor web. La versión original de
las reglas en memoria sigue disponible como referencia y para sus pruebas.

### Preparación (PowerShell, Python 3.12 o posterior)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Editar `.env` con las credenciales propias de Atlas, la URI del clúster y
`MONGODB_DATABASE=talleres_db`. Autorizar la IP pública del equipo en Atlas.
No reemplazar un `.env` ya configurado ni subirlo a Git.

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe -m proyecto.main
```

El comando alternativo `python proyecto/main.py`, usando el Python de `.venv`,
también funciona. No se necesita superusuario para el menú.

### Uso

1. Registrar participante: ingresar nombre; recibe un código como `P-001`.
2. Registrar taller: nombre, cupos positivos, inicio y fin con formato
   `AAAA-MM-DD HH:MM`, y descripción opcional. Los horarios se interpretan en UTC.
3. Consultar talleres y disponibilidad.
4. Inscribir usando códigos como `P-001` y `T-001`.
5. Consultar inscripciones confirmadas.
6. Consultar participantes.
7. Salir. Al abrir nuevamente, los datos siguen disponibles.

Las colecciones de negocio son `participantes`, `talleres` e `inscripciones`.
La colección auxiliar `contadores` asigna códigos consecutivos entre equipos.
La revisión interna del taller permite coordinar inscripciones simultáneas
mediante transacciones. Se rechazan duplicados, cupos agotados y referencias
inexistentes. No se implementan todavía espera, cancelaciones, promociones ni
restricciones de horario de inscripción.

La migración inicial adopta las colecciones que se crearon manualmente y agrega
sus índices; también funciona sobre una base nueva. No tiene reversión destructiva.
Los códigos únicos y la pareja participante/taller están protegidos por índices.
Las demás validaciones se ejecutan en los servicios: editar documentos directamente
en Atlas evita esos controles. MongoDB no impone integridad referencial entre colecciones.

### Verificación

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe tests\verificar_atlas.py
```

La última prueba requiere permisos para crear y eliminar una base temporal
`test_cli_*`. Comprueba las colecciones preexistentes, las reglas, la concurrencia
y la persistencia entre procesos del menú. Elimina solo esa base temporal al
finalizar; no introduce datos de prueba en `talleres_db`.
