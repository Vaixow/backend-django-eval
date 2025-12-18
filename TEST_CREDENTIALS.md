# Credenciales de Prueba

Para probar la aplicación en desarrollo, usa estas credenciales:

## Usuarios de Prueba

### Usuario Administrador
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **Email:** admin@taskmaster.com

### Usuario Demo
- **Usuario:** `demo`
- **Contraseña:** `demo123`
- **Email:** demo@taskmaster.com

## Datos Precargados

La base de datos incluye:
- 15 tareas de ejemplo con diferentes prioridades y estados
- Tareas asignadas a ambos usuarios
- Datos de los últimos 7 días para el dashboard

## Cómo Inicializar los Datos

Si necesitas regenerar los datos de prueba:

```bash
python manage.py shell < create_test_data.py
```

## Panel de Administración

Accede al panel de administración de Django:

**URL:** http://localhost:8000/admin/

Usa las credenciales del usuario `admin` para acceder.

Desde el admin puedes:
- Ver todas las tareas
- Crear/editar/eliminar tareas
- Gestionar usuarios
- Ver logs de la aplicación

## API Endpoints de Prueba

### 1. Obtener Token JWT

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### 2. Listar Tareas

```bash
# Reemplaza YOUR_TOKEN con el token obtenido arriba
curl http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 3. Crear Tarea

```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi nueva tarea",
    "description": "Descripción de la tarea",
    "priority": "high",
    "status": "pending"
  }'
```

## Frontend de Prueba

1. Inicia el servidor: `daphne -b 0.0.0.0 -p 8000 backend.asgi:application`
2. Abre tu navegador en: http://localhost:8000/
3. Haz clic en "Ingresar" e introduce las credenciales de `admin` o `demo`
4. Explora las funcionalidades:
   - Crear tareas desde la página principal
   - Ver el dashboard con gráficos
   - Probar el chat en tiempo real (abre dos ventanas)
   - Interactuar con el chatbot de IA

## Notas Importantes

⚠️ **NUNCA** uses estas credenciales en producción. Son solo para desarrollo.

⚠️ La base de datos SQLite (db.sqlite3) está en .gitignore y no se sube al repositorio.

⚠️ En producción, crea un superusuario nuevo con contraseña segura:
```bash
python manage.py createsuperuser
```
