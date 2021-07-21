"""Этот модуль отвечает за модели"""
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Plant(models.Model):
    name = models.CharField(max_length=20)
    datetime = models.TimeField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return(self.name)


class Action(models.Model):
    plant = models.ForeignKey(Plant, related_name='actions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='actions', on_delete=models.CASCADE)
    date = models.DateTimeField('date')
    time = models.IntegerField()
    done = models.CharField(max_length=11, default='Исполняется')
    def __str__(self):
        return(self.plant.name)
