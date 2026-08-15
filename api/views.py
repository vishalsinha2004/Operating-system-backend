# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SystemApp
from .serializers import SystemAppSerializer

@api_view(['GET'])
def get_system_apps(request):
    apps = SystemApp.objects.filter(is_active=True)
    serializer = SystemAppSerializer(apps, many=True)
    return Response(serializer.data)