# api/admin.py
from django.contrib import admin
from .models import SystemApp, SystemOS, AboutMe

@admin.register(SystemApp)
class SystemAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'app_id', 'project_type', 'is_active')
    list_filter = ('project_type', 'is_active')

@admin.register(SystemOS)
class SystemOSAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'updated_at')

# --- NEW: Register About Me ---
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')