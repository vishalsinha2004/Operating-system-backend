from rest_framework import serializers
from .models import SystemApp

class SystemAppSerializer(serializers.ModelSerializer):
    # This ensures the API outputs the raw Supabase image URL
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SystemApp
        fields = ['id', 'app_id', 'name', 'icon', 'is_active']

    def get_icon(self, obj):
        if obj.icon:
            return obj.icon.url
        return None