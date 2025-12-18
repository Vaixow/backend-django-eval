from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import Task
from .serializers import (
    TaskSerializer, TaskCreateSerializer,
    UserSerializer, UserRegistrationSerializer
)
import openai
from django.conf import settings

class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet para el CRUD completo de Tareas"""
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """Filtrar tareas por usuario si se especifica el parámetro"""
        queryset = Task.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(created_by_id=user_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        """Endpoint para obtener solo las tareas del usuario autenticado"""
        tasks = Task.objects.filter(created_by=request.user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Endpoint para registrar nuevos usuarios"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'Usuario creado exitosamente',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chatbot(request):
    """Endpoint para integración con OpenAI ChatGPT"""
    message = request.data.get('message', '')
    
    if not message:
        return Response(
            {'error': 'El mensaje es requerido'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Verificar si hay API key configurada
    if not settings.OPENAI_API_KEY:
        # Respuesta simulada si no hay API key
        return Response({
            'response': f'Chatbot (modo demo): Recibí tu mensaje "{message}". Esta es una respuesta simulada. Para usar OpenAI real, configura OPENAI_API_KEY en las variables de entorno.'
        })
    
    try:
        openai.api_key = settings.OPENAI_API_KEY
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil para gestión de tareas y productividad."},
                {"role": "user", "content": message}
            ],
            max_tokens=150
        )
        
        bot_response = response.choices[0].message.content
        
        return Response({
            'response': bot_response
        })
    except Exception as e:
        return Response({
            'error': f'Error al comunicarse con OpenAI: {str(e)}',
            'response': f'Chatbot (modo demo por error): Recibí tu mensaje "{message}". Ocurrió un error al conectar con OpenAI.'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Endpoint para obtener el perfil del usuario autenticado"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
