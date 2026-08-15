# api/serializers.py
from rest_framework import serializers
from .models import SystemApp

class SystemAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemApp
        fields = ['id', 'app_id', 'name', 'icon', 'is_active']