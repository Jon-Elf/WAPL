from django.core.management.base import BaseCommand, CommandError
from polls.models import Action, Plant
import time
import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
    end_tasks = []
    last_task = 0
    already = []
    day = ''
    def activate(self, numb, time, action):
        self.end_tasks.append({'numb': numb, 'time': time, 'action': action})
        print('\n\nклапан %s активирован\n\n' % numb)

    def disactivate(self, task):
        self.end_tasks.remove(task)
        task['action'].done = 'Завершён'
        task['action'].save()
        print('\n\nклапан %s дизактивирован\n\n' % task['numb'])

    def check_end_tasks(self, end_tasks):
        for task in end_tasks:
            task['time']-=0.5
            if task['time'] < 0.1:
                self.disactivate(task)

    def check_plant_time(self, plants):
        for plant in plants.objects.all():
            if plant not in self.already:
                if str(plant.datetime)[:-3] == time.strftime('%H:%M', time.localtime()):
                    new_action = Action(plant=plant, user=User.objects.all()[0],
                                        done='Исполняется', time=plant.time, date = datetime.datetime.now())
                    new_action.save()
                    self.already.append(plant)

    def check_next_day(self):
        if self.day != time.strftime('%d', time.localtime()):
            self.day = time.strftime('%d', time.localtime())
            self.already = []

    def handle(self, *args, **options):
        print('\n\nзапускаюсь\n\n')
        while True:
            time.sleep(0.5)
            self.check_next_day
            self.check_end_tasks(self.end_tasks)
            for action in Action.objects.filter(done='Исполняется', pk__gt=self.last_task):
                print('\n\nнашёл новое событие!\n\n')
                self.activate(action.plant.numb, action.time, action)
                self.last_task=action.pk
            self.check_plant_time(Plant)
