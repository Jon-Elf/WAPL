"""модуль для настройки админки"""
from django.contrib import admin
from .models import Plant, Action

admin.site.register(Plant)
admin.site.register(Action)
