# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('system-apps/', views.get_system_apps, name='get_system_apps'),
    
    # --- NEW: System OS Endpoint ---
    path('system-os/', views.get_system_os, name='get_system_os'),
]