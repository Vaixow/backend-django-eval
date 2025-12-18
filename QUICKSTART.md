# 🚀 Inicio Rápido - TaskMaster

## Instalación en 5 Pasos

### 1. Clonar y Entrar al Repositorio
```bash
git clone https://github.com/Vaixow/backend-django-eval.git
cd backend-django-eval
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno (Opcional)
```bash
cp .env.example .env
# Editar .env si es necesario
```

### 4. Ejecutar Migraciones y Crear Datos
```bash
python manage.py migrate
python manage.py shell < create_test_data.py
```

### 5. Iniciar Servidor
```bash
daphne -b 0.0.0.0 -p 8000 backend.asgi:application
```

## Acceder a la Aplicación

- **Frontend:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/
- **API:** http://localhost:8000/api/

## Credenciales de Prueba

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| admin   | admin123   | Administrador |
| demo    | demo123    | Usuario Demo |

## Funcionalidades Principales

### 1. Gestión de Tareas (Home)
- Crear, ver, editar tareas
- Filtrar por prioridad y estado
- Chatbot con IA

### 2. Dashboard
- Gráficos de productividad
- Estadísticas en tiempo real
- 4 tipos de visualizaciones

### 3. Chat en Vivo
- Comunicación en tiempo real
- WebSockets
- Múltiples usuarios

## Endpoints API Rápidos

### Obtener Token JWT
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### Listar Tareas
```bash
curl http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Crear Tarea
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nueva tarea",
    "description": "Descripción",
    "priority": "high"
  }'
```

## Problemas Comunes

### Error: ModuleNotFoundError
```bash
# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: No such table
```bash
# Ejecutar migraciones
python manage.py migrate
```

### Puerto 8000 en uso
```bash
# Usar otro puerto
daphne -b 0.0.0.0 -p 8001 backend.asgi:application
```

## Documentación Completa

Para más información, consulta:

- 📖 [README.md](README.md) - Documentación completa
- 🔌 [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Documentación de API
- 🚀 [DEPLOY_RENDER.md](DEPLOY_RENDER.md) - Guía de despliegue
- 🎬 [ELEVATOR_PITCH.md](ELEVATOR_PITCH.md) - Script para video
- 📊 [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) - Visión general

## Despliegue Rápido en Render

1. Crear cuenta en [Render](https://render.com/)
2. Conectar repositorio de GitHub
3. Configurar variables de entorno
4. ¡Desplegar! (automático con render.yaml)

Ver [DEPLOY_RENDER.md](DEPLOY_RENDER.md) para instrucciones detalladas.

## Stack Tecnológico

- **Backend:** Django 4.2.7, DRF, JWT
- **Frontend:** HTML5, Bootstrap 5, Chart.js
- **Tiempo Real:** Django Channels, WebSockets
- **IA:** OpenAI ChatGPT
- **Despliegue:** Render, Daphne

## ¿Necesitas Ayuda?

- 📚 Revisa la [documentación completa](README.md)
- 🐛 Abre un [issue en GitHub](https://github.com/Vaixow/backend-django-eval/issues)
- 💡 Consulta [TEST_CREDENTIALS.md](TEST_CREDENTIALS.md) para ejemplos

---

**¡Disfruta usando TaskMaster!** 🎉
