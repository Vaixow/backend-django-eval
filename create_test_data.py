"""
Script para crear datos de prueba en la base de datos
Ejecutar con: python manage.py shell < create_test_data.py
"""

from django.contrib.auth.models import User
from api.models import Task
from datetime import datetime, timedelta
import random

# Crear usuarios de prueba
print("Creando usuarios de prueba...")

users_data = [
    {'username': 'admin', 'email': 'admin@taskmaster.com', 'password': 'admin123', 'first_name': 'Admin', 'last_name': 'User'},
    {'username': 'demo', 'email': 'demo@taskmaster.com', 'password': 'demo123', 'first_name': 'Demo', 'last_name': 'User'},
]

users = []
for user_data in users_data:
    password = user_data.pop('password')
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults=user_data
    )
    if created:
        user.set_password(password)
        user.save()
        print(f"✓ Usuario creado: {user.username}")
    else:
        print(f"- Usuario ya existe: {user.username}")
    users.append(user)

# Crear tareas de prueba
print("\nCreando tareas de prueba...")

tasks_data = [
    {'title': 'Implementar autenticación JWT', 'description': 'Configurar Simple JWT para la API REST', 'priority': 'high', 'status': 'completed'},
    {'title': 'Crear dashboard con Chart.js', 'description': 'Diseñar y desarrollar dashboard con gráficos interactivos', 'priority': 'high', 'status': 'completed'},
    {'title': 'Integrar OpenAI ChatGPT', 'description': 'Implementar chatbot con API de OpenAI', 'priority': 'high', 'status': 'completed'},
    {'title': 'Configurar WebSockets', 'description': 'Implementar chat en tiempo real con Django Channels', 'priority': 'high', 'status': 'completed'},
    {'title': 'Diseñar interfaz de usuario', 'description': 'Crear templates HTML con Bootstrap 5', 'priority': 'medium', 'status': 'completed'},
    {'title': 'Configurar CORS', 'description': 'Implementar django-cors-headers de manera segura', 'priority': 'medium', 'status': 'completed'},
    {'title': 'Documentar API', 'description': 'Escribir documentación completa de endpoints', 'priority': 'medium', 'status': 'in_progress'},
    {'title': 'Preparar despliegue en Render', 'description': 'Crear render.yaml y build.sh', 'priority': 'high', 'status': 'in_progress'},
    {'title': 'Escribir README completo', 'description': 'Documentación del proyecto con instrucciones', 'priority': 'medium', 'status': 'in_progress'},
    {'title': 'Pruebas de integración', 'description': 'Probar todas las funcionalidades end-to-end', 'priority': 'high', 'status': 'pending'},
    {'title': 'Optimizar rendimiento', 'description': 'Mejorar tiempos de respuesta de la API', 'priority': 'low', 'status': 'pending'},
    {'title': 'Agregar tests unitarios', 'description': 'Implementar suite de tests para models y views', 'priority': 'medium', 'status': 'pending'},
    {'title': 'Configurar CI/CD', 'description': 'Automatizar despliegue con GitHub Actions', 'priority': 'low', 'status': 'pending'},
    {'title': 'Implementar paginación avanzada', 'description': 'Mejorar paginación en listados grandes', 'priority': 'low', 'status': 'pending'},
    {'title': 'Agregar filtros de búsqueda', 'description': 'Filtros avanzados por fecha, prioridad, etc.', 'priority': 'medium', 'status': 'pending'},
]

for i, task_data in enumerate(tasks_data):
    # Asignar usuario alternando
    task_data['created_by'] = users[i % len(users)]
    
    # Asignar fecha de vencimiento aleatoria
    days_ahead = random.randint(1, 30)
    task_data['due_date'] = (datetime.now() + timedelta(days=days_ahead)).date()
    
    task, created = Task.objects.get_or_create(
        title=task_data['title'],
        defaults=task_data
    )
    if created:
        print(f"✓ Tarea creada: {task.title}")
    else:
        print(f"- Tarea ya existe: {task.title}")

print("\n" + "="*50)
print("DATOS DE PRUEBA CREADOS EXITOSAMENTE")
print("="*50)
print("\nCredenciales de prueba:")
print("Usuario: admin | Contraseña: admin123")
print("Usuario: demo | Contraseña: demo123")
print("\nTotal de tareas creadas:", Task.objects.count())
print("="*50)
