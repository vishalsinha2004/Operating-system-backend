# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SystemApp, SystemOS, AboutMe
from .serializers import SystemAppSerializer, SystemOSSerializer, AboutMeSerializer

@api_view(['GET'])
def get_system_apps(request):
    apps = SystemApp.objects.filter(is_active=True)
    serializer = SystemAppSerializer(apps, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_system_os(request):
    system_os_data = SystemOS.objects.all()
    serializer = SystemOSSerializer(system_os_data, many=True, context={'request': request})
    return Response(serializer.data)

# --- NEW: About Me View ---
@api_view(['GET'])
def get_about_me(request):
    about_data = AboutMe.objects.all()
    serializer = AboutMeSerializer(about_data, many=True, context={'request': request})
    return Response(serializer.data)