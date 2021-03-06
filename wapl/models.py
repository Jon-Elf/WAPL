import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Plant(models.Model):
    ordering = ['-name']
    name = models.CharField(max_length=20)
    datetime = models.TimeField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    numb = models.IntegerField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return(self.name)
    def last_watering(self):
        if self.actions.first():
            return(self.actions.last().date)
        return None

class Action(models.Model):
    ordering = ['-date']
    plant = models.ForeignKey(Plant, related_name='actions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='actions', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField('date')
    time = models.IntegerField()
    done = models.CharField(max_length=11, default='in progress')
    def __str__(self):
        return self.plant.name

class Channel(models.Model):
	ordering=['-number']
	number=models.IntegerField()
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return str(self.number)
