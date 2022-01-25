"""модуль для настройки админки"""
from django.contrib import admin
from .models import Plant, Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ('plant', 'date', 'time', 'user', 'done')
    list_filter = ('plant', 'date', 'user')

admin.site.register(Plant)
admin.site.register(Action, ActionAdmin)
