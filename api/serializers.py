from rest_framework import serializers
from .models import SystemApp, SystemOS, AboutMe

class SystemAppSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SystemApp
        fields = [
            'id', 'app_id', 'name', 'icon', 
            'description', 'tech_stack', 
            'frontend_repo', 'backend_repo', 'live_link', 
            'project_type', 
            'is_active'
        ]

    def get_icon(self, obj):
        if obj.icon:
            return obj.icon.url
        return None


class SystemOSSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SystemOS
        fields = '__all__'
        
    def get_icon(self, obj):
        if obj.icon:
            return obj.icon.url
        return None


# --- NEW: About Me Serializer ---
class AboutMeSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = AboutMe
        fields = '__all__'
        
    def get_profile_image(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None