# api/admin.py
from django.contrib import admin
from .models import SystemApp, SystemOS

@admin.register(SystemApp)
class SystemAppAdmin(admin.ModelAdmin):
    # Display the project type in the admin table and allow filtering
    list_display = ('name', 'app_id', 'project_type', 'is_active')
    list_filter = ('project_type', 'is_active')

@admin.register(SystemOS)
class SystemOSAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'updated_at')