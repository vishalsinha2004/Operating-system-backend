# api/admin.py
from django.contrib import admin
from .models import SystemApp

admin.site.register(SystemApp)