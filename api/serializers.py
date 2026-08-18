from rest_framework import serializers
from .models import SystemApp

class SystemAppSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SystemApp
        # Added the new fields to the API output
        fields = [
            'id', 'app_id', 'name', 'icon', 
            'description', 'tech_stack', 
            'frontend_repo', 'backend_repo', 'live_link', 
            'is_active'
        ]

    def get_icon(self, obj):
        if obj.icon:
            return obj.icon.url
        return None