# Guía de Despliegue en Render

Esta guía te ayudará a desplegar TaskMaster en Render paso a paso.

## Prerrequisitos

1. Una cuenta en [Render](https://render.com/) (es gratuita)
2. Tu repositorio de GitHub conectado a Render
3. (Opcional) Una API key de OpenAI para el chatbot

## Pasos para el Despliegue

### 1. Conectar tu Repositorio

1. Inicia sesión en [Render Dashboard](https://dashboard.render.com/)
2. Haz clic en **"New +"** y selecciona **"Web Service"**
3. Conecta tu repositorio de GitHub: `Vaixow/backend-django-eval`
4. Selecciona la rama `main` o la rama que desees desplegar

### 2. Configuración del Servicio

Render detectará automáticamente el archivo `render.yaml` en tu repositorio. Si no lo hace, configura manualmente:

- **Name:** `taskmaster-backend` (o el nombre que prefieras)
- **Region:** Oregon (o la región más cercana)
- **Branch:** `main`
- **Runtime:** Python 3
- **Build Command:** `./build.sh`
- **Start Command:** `daphne -b 0.0.0.0 -p $PORT backend.asgi:application`

### 3. Configurar Variables de Entorno

En la sección de **Environment Variables**, agrega las siguientes variables:

#### Variables Obligatorias:

```
SECRET_KEY=genera-una-clave-secreta-aqui-muy-larga-y-aleatoria
DEBUG=False
ALLOWED_HOSTS=.onrender.com
```

#### Variables Opcionales:

```
OPENAI_API_KEY=tu-api-key-de-openai-aqui
CORS_ALLOWED_ORIGINS=https://tu-dominio.onrender.com
CSRF_TRUSTED_ORIGINS=https://tu-dominio.onrender.com
```

### 4. Generar SECRET_KEY

Para generar una SECRET_KEY segura, puedes usar Python:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

O usar un generador online de claves secretas (asegúrate de que sea seguro).

### 5. Configuración de Base de Datos (Opcional)

Por defecto, TaskMaster usa SQLite. Para producción seria, se recomienda PostgreSQL:

1. En Render, crea un nuevo **PostgreSQL Database**
2. Copia la **Internal Database URL**
3. Agrega como variable de entorno:
   ```
   DATABASE_URL=postgres://usuario:password@host:puerto/database
   ```
4. El archivo `settings.py` ya está configurado para usar `DATABASE_URL` si está presente

### 6. Desplegar

1. Haz clic en **"Create Web Service"** o **"Deploy"**
2. Render comenzará a:
   - Clonar tu repositorio
   - Ejecutar `./build.sh` (instala dependencias, colecta estáticos, ejecuta migraciones)
   - Iniciar el servidor con Daphne

### 7. Verificar el Despliegue

Una vez completado el despliegue:

1. Render te proporcionará una URL como: `https://taskmaster-backend.onrender.com`
2. Accede a tu aplicación en esa URL
3. Verifica que puedas:
   - Ver la página principal
   - Registrar un usuario
   - Iniciar sesión
   - Crear tareas
   - Acceder al dashboard
   - Usar el chat en tiempo real

### 8. Actualizar CORS y CSRF

Después del primer despliegue, actualiza las variables de entorno con tu URL real:

```
ALLOWED_HOSTS=.onrender.com,taskmaster-backend.onrender.com
CORS_ALLOWED_ORIGINS=https://taskmaster-backend.onrender.com
CSRF_TRUSTED_ORIGINS=https://taskmaster-backend.onrender.com
```

## Configuración Avanzada

### Usar PostgreSQL en Producción

1. Crear una base de datos PostgreSQL en Render
2. Agregar la URL a las variables de entorno
3. Instalar el adaptador (ya incluido en requirements.txt):
   ```
   psycopg2-binary==2.9.9
   ```

### Configurar Redis para WebSockets (Opcional)

Para producción con múltiples instancias, se recomienda Redis:

1. Crear un Redis en Render o usar un servicio externo
2. Actualizar `settings.py`:
   ```python
   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               "hosts": [('redis-host', 6379)],
           },
       },
   }
   ```

### Logs y Monitoreo

- Los logs están disponibles en el Dashboard de Render
- Puedes ver logs en tiempo real o históricos
- Configura alertas para errores

## Comandos Útiles

### Ejecutar Migraciones Manualmente

Si necesitas ejecutar migraciones después del despliegue:

```bash
python manage.py migrate
```

### Crear Superusuario en Producción

Conecta a tu instancia y ejecuta:

```bash
python manage.py createsuperuser
```

### Recopilar Archivos Estáticos

```bash
python manage.py collectstatic --no-input
```

## Troubleshooting

### Error: "Application failed to start"

- Verifica los logs en el Dashboard de Render
- Asegúrate de que todas las dependencias estén en `requirements.txt`
- Verifica que `build.sh` tenga permisos de ejecución

### Error: "ALLOWED_HOSTS"

- Agrega tu dominio de Render a `ALLOWED_HOSTS`
- Ejemplo: `ALLOWED_HOSTS=.onrender.com,taskmaster-backend.onrender.com`

### WebSockets no funcionan

- Verifica que estés usando `daphne` en el start command
- Asegúrate de que el protocolo sea `wss://` (no `ws://`) en producción

### Archivos estáticos no se cargan

- Verifica que `collectstatic` se ejecutó en `build.sh`
- Asegúrate de que WhiteNoise esté configurado correctamente
- Revisa la configuración de `STATIC_ROOT` y `STATIC_URL`

## Costos

- **Plan Free:** Suficiente para desarrollo y demos
  - 750 horas/mes de uso
  - Se duerme después de 15 minutos de inactividad
  - Se despierta automáticamente con la primera petición

- **Plan Starter ($7/mes):** Para producción
  - Siempre activo
  - Más recursos
  - Sin tiempo de inactividad

## Mantenimiento

### Actualizaciones Automáticas

Render puede configurarse para redesplegar automáticamente cuando haces push a tu rama principal:

1. Ve a **Settings** en tu servicio
2. En **Build & Deploy**, habilita **Auto-Deploy**
3. Cada push a `main` disparará un nuevo despliegue

### Despliegue Manual

Si prefieres controlar cuándo desplegar:

1. Ve a tu servicio en Render
2. Haz clic en **"Manual Deploy"**
3. Selecciona la rama o commit específico

## Recursos Adicionales

- [Documentación de Render](https://render.com/docs)
- [Documentación de Django Deployment](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Django Channels Deployment](https://channels.readthedocs.io/en/stable/deploying.html)

## Soporte

Si encuentras problemas:

1. Revisa los logs en el Dashboard de Render
2. Consulta la [documentación de Render](https://render.com/docs)
3. Abre un issue en el repositorio de GitHub

---

¡Felicidades! Tu aplicación TaskMaster está ahora desplegada en producción. 🚀
