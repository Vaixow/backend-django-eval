from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Task
from django.contrib.auth.models import User
from django.db.models import Count, Q
from datetime import datetime, timedelta
import random

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Endpoint con estadísticas para el dashboard"""
    user = request.user
    
    # Estadísticas de tareas del usuario
    total_tasks = Task.objects.filter(created_by=user).count()
    completed_tasks = Task.objects.filter(created_by=user, status='completed').count()
    pending_tasks = Task.objects.filter(created_by=user, status='pending').count()
    in_progress_tasks = Task.objects.filter(created_by=user, status='in_progress').count()
    
    # Tareas por prioridad
    high_priority = Task.objects.filter(created_by=user, priority='high').count()
    medium_priority = Task.objects.filter(created_by=user, priority='medium').count()
    low_priority = Task.objects.filter(created_by=user, priority='low').count()
    
    # Tareas por día de la última semana
    today = datetime.now().date()
    week_data = []
    for i in range(6, -1, -1):
        date = today - timedelta(days=i)
        count = Task.objects.filter(
            created_by=user,
            created_at__date=date
        ).count()
        week_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'count': count
        })
    
    return Response({
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
        'week_data': week_data,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_chart_data(request):
    """Endpoint con datos simulados para gráficos de Chart.js"""
    
    # Datos de productividad mensual (simulados)
    months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    current_month = datetime.now().month
    
    # Datos del año actual
    productivity_data = []
    for i in range(12):
        if i < current_month:
            # Datos históricos (simulados con tendencia creciente)
            productivity_data.append(random.randint(10, 30) + i * 2)
        else:
            productivity_data.append(0)
    
    # Datos de tareas por categoría (simulados)
    categories = {
        'Trabajo': random.randint(15, 35),
        'Personal': random.randint(10, 25),
        'Estudio': random.randint(5, 20),
        'Proyectos': random.randint(8, 22),
        'Otros': random.randint(3, 15)
    }
    
    # Tendencia semanal (simulados)
    days = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    tasks_created = [random.randint(3, 12) for _ in range(7)]
    tasks_completed = [random.randint(2, 10) for _ in range(7)]
    
    return Response({
        'productivity': {
            'labels': months[:current_month],
            'data': productivity_data[:current_month]
        },
        'categories': {
            'labels': list(categories.keys()),
            'data': list(categories.values())
        },
        'weekly_trend': {
            'labels': days,
            'tasks_created': tasks_created,
            'tasks_completed': tasks_completed
        }
    })
