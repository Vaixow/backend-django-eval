# Documentación de API - TaskMaster

API RESTful completa para gestión de tareas con autenticación JWT.

**Base URL:** `http://localhost:8000/api/` (desarrollo) o `https://tu-app.onrender.com/api/` (producción)

## Tabla de Contenidos

1. [Autenticación](#autenticación)
2. [Tareas (Tasks)](#tareas-tasks)
3. [Dashboard](#dashboard)
4. [Chatbot](#chatbot)
5. [Perfil de Usuario](#perfil-de-usuario)
6. [Códigos de Respuesta](#códigos-de-respuesta)
7. [Ejemplos con cURL](#ejemplos-con-curl)
8. [Ejemplos con JavaScript](#ejemplos-con-javascript)

---

## Autenticación

TaskMaster usa **JWT (JSON Web Tokens)** para autenticación.

### Registrar Usuario

Crea una nueva cuenta de usuario.

**Endpoint:** `POST /api/auth/register/`

**Permisos:** Público (no requiere autenticación)

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securePassword123",
  "password2": "securePassword123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201 Created):**
```json
{
  "message": "Usuario creado exitosamente",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

**Errores:**
- `400 Bad Request`: Las contraseñas no coinciden o el usuario ya existe

---

### Iniciar Sesión (Login)

Obtiene tokens de acceso y refresco.

**Endpoint:** `POST /api/auth/login/`

**Permisos:** Público

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Uso del Token:**
- El token `access` debe incluirse en todas las peticiones autenticadas
- Header: `Authorization: Bearer {access_token}`
- El token `access` expira en 60 minutos
- Usa el token `refresh` para obtener un nuevo `access` token

---

### Refrescar Token

Obtiene un nuevo token de acceso usando el token de refresco.

**Endpoint:** `POST /api/auth/refresh/`

**Permisos:** Público

**Request Body:**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## Tareas (Tasks)

CRUD completo para gestión de tareas.

### Listar Todas las Tareas

**Endpoint:** `GET /api/tasks/`

**Permisos:** Requiere autenticación

**Query Parameters:**
- `page` (opcional): Número de página (default: 1)
- `user` (opcional): Filtrar por ID de usuario

**Response (200 OK):**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/tasks/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Implementar autenticación JWT",
      "description": "Configurar Simple JWT para la API REST",
      "priority": "high",
      "status": "completed",
      "created_by": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe"
      },
      "created_at": "2024-12-17T10:30:00Z",
      "updated_at": "2024-12-17T15:45:00Z",
      "due_date": "2024-12-20"
    }
  ]
}
```

---

### Obtener Mis Tareas

Obtiene solo las tareas del usuario autenticado.

**Endpoint:** `GET /api/tasks/my_tasks/`

**Permisos:** Requiere autenticación

**Response:** Igual que listar tareas, pero filtradas por el usuario actual.

---

### Obtener Tarea Específica

**Endpoint:** `GET /api/tasks/{id}/`

**Permisos:** Requiere autenticación

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Implementar autenticación JWT",
  "description": "Configurar Simple JWT para la API REST",
  "priority": "high",
  "status": "completed",
  "created_by": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "created_at": "2024-12-17T10:30:00Z",
  "updated_at": "2024-12-17T15:45:00Z",
  "due_date": "2024-12-20"
}
```

**Errores:**
- `404 Not Found`: La tarea no existe

---

### Crear Tarea

**Endpoint:** `POST /api/tasks/`

**Permisos:** Requiere autenticación

**Request Body:**
```json
{
  "title": "Nueva tarea",
  "description": "Descripción detallada de la tarea",
  "priority": "medium",
  "status": "pending",
  "due_date": "2024-12-25"
}
```

**Campos:**
- `title` (requerido): Título de la tarea (máx. 200 caracteres)
- `description` (requerido): Descripción de la tarea
- `priority` (opcional): `"low"`, `"medium"`, o `"high"` (default: `"medium"`)
- `status` (opcional): `"pending"`, `"in_progress"`, o `"completed"` (default: `"pending"`)
- `due_date` (opcional): Fecha de vencimiento en formato `YYYY-MM-DD`

**Response (201 Created):**
```json
{
  "id": 2,
  "title": "Nueva tarea",
  "description": "Descripción detallada de la tarea",
  "priority": "medium",
  "status": "pending",
  "created_by": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "created_at": "2024-12-17T16:00:00Z",
  "updated_at": "2024-12-17T16:00:00Z",
  "due_date": "2024-12-25"
}
```

---

### Actualizar Tarea

**Endpoint:** `PUT /api/tasks/{id}/` (actualización completa) o `PATCH /api/tasks/{id}/` (actualización parcial)

**Permisos:** Requiere autenticación

**Request Body (PUT - todos los campos requeridos):**
```json
{
  "title": "Tarea actualizada",
  "description": "Nueva descripción",
  "priority": "high",
  "status": "in_progress",
  "due_date": "2024-12-30"
}
```

**Request Body (PATCH - campos opcionales):**
```json
{
  "status": "completed"
}
```

**Response (200 OK):** Objeto de tarea actualizado

---

### Eliminar Tarea

**Endpoint:** `DELETE /api/tasks/{id}/`

**Permisos:** Requiere autenticación

**Response (204 No Content):** Sin contenido

---

## Dashboard

Endpoints para obtener estadísticas y datos para gráficos.

### Estadísticas

Obtiene estadísticas generales de las tareas del usuario.

**Endpoint:** `GET /api/dashboard/stats/`

**Permisos:** Requiere autenticación

**Response (200 OK):**
```json
{
  "total_tasks": 15,
  "completed_tasks": 8,
  "pending_tasks": 5,
  "in_progress_tasks": 2,
  "high_priority": 3,
  "medium_priority": 8,
  "low_priority": 4,
  "week_data": [
    {
      "date": "2024-12-11",
      "count": 2
    },
    {
      "date": "2024-12-12",
      "count": 3
    }
  ]
}
```

---

### Datos para Gráficos

Obtiene datos formateados para Chart.js.

**Endpoint:** `GET /api/dashboard/chart-data/`

**Permisos:** Requiere autenticación

**Response (200 OK):**
```json
{
  "productivity": {
    "labels": ["Ene", "Feb", "Mar", "Abr", "May"],
    "data": [12, 19, 15, 25, 22]
  },
  "categories": {
    "labels": ["Trabajo", "Personal", "Estudio", "Proyectos", "Otros"],
    "data": [25, 18, 12, 20, 8]
  },
  "weekly_trend": {
    "labels": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
    "tasks_created": [5, 7, 4, 9, 6, 3, 2],
    "tasks_completed": [3, 5, 4, 7, 5, 2, 1]
  }
}
```

---

## Chatbot

Integración con OpenAI ChatGPT.

### Enviar Mensaje al Chatbot

**Endpoint:** `POST /api/chatbot/`

**Permisos:** Requiere autenticación

**Request Body:**
```json
{
  "message": "¿Cómo puedo mejorar mi productividad?"
}
```

**Response (200 OK):**
```json
{
  "response": "Para mejorar tu productividad, te recomiendo: 1) Establece objetivos claros..."
}
```

**Nota:** Si no hay una API key de OpenAI configurada, el endpoint responderá con un mensaje simulado.

---

## Perfil de Usuario

### Obtener Perfil

**Endpoint:** `GET /api/profile/`

**Permisos:** Requiere autenticación

**Response (200 OK):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```

---

## Códigos de Respuesta

| Código | Descripción |
|--------|-------------|
| 200 OK | Petición exitosa |
| 201 Created | Recurso creado exitosamente |
| 204 No Content | Petición exitosa sin contenido |
| 400 Bad Request | Datos inválidos |
| 401 Unauthorized | No autenticado o token inválido |
| 403 Forbidden | No tiene permisos |
| 404 Not Found | Recurso no encontrado |
| 500 Internal Server Error | Error del servidor |

---

## Ejemplos con cURL

### Registrar usuario
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securePassword123",
    "password2": "securePassword123"
  }'
```

### Iniciar sesión
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securePassword123"
  }'
```

### Listar tareas
```bash
TOKEN="tu_access_token_aqui"
curl http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer $TOKEN"
```

### Crear tarea
```bash
TOKEN="tu_access_token_aqui"
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nueva tarea",
    "description": "Descripción",
    "priority": "high"
  }'
```

---

## Ejemplos con JavaScript

### Registrar usuario
```javascript
async function register() {
  const response = await fetch('http://localhost:8000/api/auth/register/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'johndoe',
      email: 'john@example.com',
      password: 'securePassword123',
      password2: 'securePassword123'
    })
  });
  const data = await response.json();
  console.log(data);
}
```

### Iniciar sesión
```javascript
async function login() {
  const response = await fetch('http://localhost:8000/api/auth/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'johndoe',
      password: 'securePassword123'
    })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  localStorage.setItem('refresh_token', data.refresh);
  return data;
}
```

### Listar tareas
```javascript
async function getTasks() {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/api/tasks/', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  const data = await response.json();
  return data.results;
}
```

### Crear tarea
```javascript
async function createTask(taskData) {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/api/tasks/', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(taskData)
  });
  const data = await response.json();
  return data;
}
```

### Usar el chatbot
```javascript
async function askChatbot(message) {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/api/chatbot/', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  });
  const data = await response.json();
  return data.response;
}
```

---

## Paginación

Todos los endpoints de listado soportan paginación:

- `page`: Número de página (default: 1)
- `page_size`: Tareas por página (default: 10, max: 100)

Ejemplo: `GET /api/tasks/?page=2&page_size=20`

---

## Manejo de Errores

Todos los errores devuelven JSON con detalles:

```json
{
  "detail": "Descripción del error",
  "field_name": ["Error específico del campo"]
}
```

---

Para más información, consulta el [README.md](README.md) del proyecto.
