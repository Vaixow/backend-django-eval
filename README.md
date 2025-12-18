# TaskMaster - Gestión Inteligente de Tareas con IA

![Django](https://img.shields.io/badge/Django-4.2.7-green)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![WebSockets](https://img.shields.io/badge/WebSockets-Channels-orange)

## 🚀 URL de Producción

**Deploy en Render:** [Próximamente - Configurar en Render]

## 📋 Descripción del Proyecto

TaskMaster es una aplicación web completa de gestión de tareas que integra las siguientes tecnologías modernas:

- **Backend:** Django 4.2 con Django REST Framework
- **Autenticación:** JWT (JSON Web Tokens) con Simple JWT
- **Inteligencia Artificial:** Integración con OpenAI ChatGPT
- **Comunicación en Tiempo Real:** WebSockets con Django Channels
- **Visualización de Datos:** Dashboard interactivo con Chart.js
- **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript vanilla
- **Despliegue:** Render (PaaS)

## ✨ Características Principales

### 1. API REST Completa
- ✅ CRUD completo para gestión de tareas
- ✅ Autenticación JWT
- ✅ Paginación y filtros
- ✅ Documentación de endpoints

### 2. Integraciones Avanzadas
- 🤖 **Chatbot con IA:** Integración con OpenAI ChatGPT para asistencia inteligente
- 📊 **Dashboard Analítico:** Visualización de datos con Chart.js (4 tipos de gráficos)
- 💬 **Chat en Tiempo Real:** WebSockets para comunicación instantánea

### 3. Seguridad
- 🔒 Variables de entorno para credenciales sensibles
- 🛡️ CORS configurado de manera segura
- 🔐 Autenticación JWT con tokens de acceso y refresco
- ✅ Validación de datos en backend

### 4. Cliente Web Funcional
- 📱 Diseño responsive con Bootstrap 5
- 🎨 Interfaz moderna y atractiva
- ⚡ Comunicación asíncrona con el backend
- 🖥️ Tres páginas principales: Home, Dashboard, Chat

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.12+
- pip
- Git

### Instalación Local

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Vaixow/backend-django-eval.git
cd backend-django-eval
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

Variables necesarias:
- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: True para desarrollo, False para producción
- `ALLOWED_HOSTS`: Hosts permitidos (separados por comas)
- `OPENAI_API_KEY`: Tu API key de OpenAI (opcional, funciona en modo demo sin ella)
- `CORS_ALLOWED_ORIGINS`: Orígenes permitidos para CORS
- `CSRF_TRUSTED_ORIGINS`: Orígenes confiables para CSRF

5. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

6. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

7. **Recopilar archivos estáticos:**
```bash
python manage.py collectstatic --no-input
```

8. **Ejecutar servidor de desarrollo:**
```bash
# Con soporte para WebSockets:
daphne -b 0.0.0.0 -p 8000 backend.asgi:application

# O con el servidor de desarrollo normal (sin WebSockets):
python manage.py runserver
```

9. **Acceder a la aplicación:**
- Frontend: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- API: http://localhost:8000/api/

## 📚 Documentación de la API

### Base URL
```
http://localhost:8000/api/
```

### Autenticación

#### Registrar usuario
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "usuario",
  "email": "usuario@example.com",
  "password": "contraseña",
  "password2": "contraseña"
}
```

#### Iniciar sesión (Obtener tokens)
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "usuario",
  "password": "contraseña"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Refrescar token
```http
POST /api/auth/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Tareas (Tasks)

#### Listar todas las tareas
```http
GET /api/tasks/
Authorization: Bearer {access_token}
```

#### Obtener mis tareas
```http
GET /api/tasks/my_tasks/
Authorization: Bearer {access_token}
```

#### Crear tarea
```http
POST /api/tasks/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "title": "Mi tarea",
  "description": "Descripción de la tarea",
  "priority": "high",
  "status": "pending",
  "due_date": "2024-12-31"
}
```

#### Obtener tarea específica
```http
GET /api/tasks/{id}/
Authorization: Bearer {access_token}
```

#### Actualizar tarea
```http
PUT /api/tasks/{id}/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "title": "Tarea actualizada",
  "description": "Nueva descripción",
  "priority": "medium",
  "status": "in_progress"
}
```

#### Eliminar tarea
```http
DELETE /api/tasks/{id}/
Authorization: Bearer {access_token}
```

### Chatbot (OpenAI)

```http
POST /api/chatbot/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "message": "¿Cómo puedo mejorar mi productividad?"
}

Response:
{
  "response": "Para mejorar tu productividad..."
}
```

### Dashboard

#### Estadísticas
```http
GET /api/dashboard/stats/
Authorization: Bearer {access_token}

Response:
{
  "total_tasks": 10,
  "completed_tasks": 5,
  "pending_tasks": 3,
  "in_progress_tasks": 2,
  "high_priority": 2,
  "medium_priority": 5,
  "low_priority": 3,
  "week_data": [...]
}
```

#### Datos para gráficos
```http
GET /api/dashboard/chart-data/
Authorization: Bearer {access_token}

Response:
{
  "productivity": {...},
  "categories": {...},
  "weekly_trend": {...}
}
```

### Perfil de Usuario

```http
GET /api/profile/
Authorization: Bearer {access_token}

Response:
{
  "id": 1,
  "username": "usuario",
  "email": "usuario@example.com",
  "first_name": "",
  "last_name": ""
}
```

## 🔌 WebSockets

### Conexión al Chat en Tiempo Real

```javascript
const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const wsUrl = `${protocol}//${window.location.host}/ws/chat/general/`;
const socket = new WebSocket(wsUrl);

// Enviar mensaje
socket.send(JSON.stringify({
  'message': 'Hola a todos',
  'username': 'usuario'
}));

// Recibir mensaje
socket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  console.log(data.message);
};
```

## 🎯 Propuesta de Valor

### Problema que Resuelve
La gestión de tareas tradicional carece de:
- Asistencia inteligente para priorizar y organizar
- Análisis de productividad visual
- Colaboración en tiempo real

### Solución
TaskMaster integra:
1. **IA de OpenAI** para ayudar a los usuarios a tomar mejores decisiones sobre sus tareas
2. **Visualización de datos** para entender patrones de productividad
3. **Comunicación instantánea** para colaboración efectiva con el equipo

### Integraciones Únicas
- ✅ **OpenAI ChatGPT:** Asistente inteligente que ayuda a organizar y priorizar tareas
- ✅ **Chart.js:** 4 tipos de gráficos para análisis visual (línea, dona, barras, polar)
- ✅ **WebSockets:** Chat en tiempo real para colaboración instantánea
- ✅ **JWT Authentication:** Seguridad robusta para proteger datos de usuarios
- ✅ **Bootstrap 5:** UI moderna y responsive

## 🏗️ Arquitectura

```
backend-django-eval/
├── backend/              # Configuración principal del proyecto
│   ├── settings.py      # Configuraciones (Django, DRF, JWT, CORS, Channels)
│   ├── urls.py          # URLs principales
│   ├── asgi.py          # Configuración ASGI para WebSockets
│   └── wsgi.py          # Configuración WSGI
├── api/                 # App principal de API
│   ├── models.py        # Modelo Task
│   ├── serializers.py   # Serializers de DRF
│   ├── views.py         # ViewSets y vistas de API
│   └── urls.py          # URLs de la API
├── dashboard/           # App de dashboard
│   ├── views.py         # Vistas para estadísticas y datos de gráficos
│   └── urls.py          # URLs del dashboard
├── chat/                # App de chat en tiempo real
│   ├── consumers.py     # WebSocket consumers
│   └── routing.py       # Routing de WebSockets
├── templates/           # Templates HTML
│   ├── base.html        # Template base
│   ├── index.html       # Página principal
│   ├── dashboard.html   # Dashboard
│   └── chat.html        # Chat en vivo
├── static/              # Archivos estáticos (CSS, JS)
├── requirements.txt     # Dependencias de Python
├── render.yaml          # Configuración de Render
├── build.sh             # Script de build para producción
├── .env.example         # Ejemplo de variables de entorno
└── manage.py            # Script de gestión de Django
```

## 🚀 Despliegue en Render

1. **Crear cuenta en Render:** https://render.com/

2. **Conectar repositorio de GitHub**

3. **Configurar variables de entorno en Render:**
   - `SECRET_KEY`
   - `ALLOWED_HOSTS` (incluir `.onrender.com`)
   - `OPENAI_API_KEY` (opcional)
   - `CORS_ALLOWED_ORIGINS`
   - `CSRF_TRUSTED_ORIGINS`

4. **El despliegue se realizará automáticamente** usando `render.yaml` y `build.sh`

## 🎬 Elevator Pitch (2 minutos)

### El Problema
¿Alguna vez te has sentido abrumado por la cantidad de tareas que tienes que hacer? ¿No sabes por dónde empezar o qué priorizar? Las herramientas tradicionales de gestión de tareas son estáticas y no te ayudan a tomar decisiones inteligentes.

### Nuestra Solución
TaskMaster es una plataforma de gestión de tareas potenciada por inteligencia artificial que no solo organiza tus tareas, sino que te ayuda a ser más productivo.

### Características Clave
1. **Asistente IA con ChatGPT:** Pregúntale cómo priorizar tus tareas, obtén consejos de productividad o busca la mejor manera de abordar un proyecto complejo.

2. **Dashboard Analítico:** Visualiza tu productividad con gráficos interactivos. Identifica patrones, ve tu progreso mensual y entiende dónde inviertes tu tiempo.

3. **Chat en Tiempo Real:** Colabora con tu equipo instantáneamente con WebSockets. Sin recargas, sin esperas, comunicación real.

### Tecnología
Construido con las tecnologías más modernas:
- Backend robusto con Django y REST API
- Autenticación segura con JWT
- Integraciones avanzadas: OpenAI, Chart.js, WebSockets
- Diseño responsive con Bootstrap 5

### Valor Único
No es solo otra app de tareas. Es tu asistente personal de productividad con IA, análisis visual y colaboración en tiempo real, todo en una plataforma.

### Llamado a la Acción
¿Listo para transformar tu productividad? Prueba TaskMaster hoy.

## 📝 Licencia

Este proyecto fue desarrollado como evaluación técnica.

## 👨‍💻 Autor

Desarrollado con ❤️ usando Django, DRF, OpenAI, Channels y más.

---

**¿Preguntas o sugerencias?** Abre un issue en GitHub.
