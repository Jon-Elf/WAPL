from django.core.management.base import BaseCommand, CommandError
from wapl.models import Action, Plant, Channel
import time
import datetime
from django.contrib.auth.models import User
import RPi.GPIO as GPIO
import logging
from django.conf import settings
from os.path import splitext, basename

class Command(BaseCommand):

    end_tasks = []
    last_task = 0
    already = []
    day = ''
    

    def setup_channels(self, chan_list):
        logging.info('Начинается установка каналов %s.' % chan_list)
        GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.HIGH)
        logging.info('Каналы %s установлены.' % chan_list)

    def activate(self, numb, time, action):
        self.end_tasks.append({'numb': numb, 'time': time, 'action': action})
        self.setup_channels(numb)
        logging.info('Клапан %s (%s) активируется...' % (numb, action.plant.name))
        GPIO.output(numb, GPIO.LOW)
        logging.info('Клапан %s (%s) активирован.' % (numb, action.plant.name))

    def disactivate(self, task):
        self.end_tasks.remove(task)
        task['action'].done = 'Completed'
        task['action'].save()
        logging.info('Клапан %s (%s) дизактивируется...' % (task['numb'], task['action'].plant.name))
        GPIO.output(task['numb'], GPIO.HIGH)
        logging.info('Клапан %s (%s) дизактивирован.' % (task['numb'], task['action'].plant.name))

    def check_end_tasks(self, end_tasks):
        for task in end_tasks:
            task['time']-=0.5
            if task['time'] < 0.1:
                self.disactivate(task)

    def check_plant_time(self, plants):
        for plant in plants.objects.filter(is_active=True):
            if plant not in self.already:
                if str(plant.datetime)[:-3] == time.strftime('%H:%M', time.localtime()):
                    logging.info('У растения %s (клапан %s) время авт. полива.' % (plant.name, plant.numb))
                    new_action = Action(plant=plant,
                                        done='in progress', time=plant.time, date = datetime.datetime.now())
                    new_action.save()
                    self.already.append(plant)

    def check_next_day(self):
        if self.day != time.strftime('%d', time.localtime()):
            logging.info('Список "already" сбрасывается, так как сменился день.')
            self.day = time.strftime('%d', time.localtime())
            self.already = []

    def handle(self, *args, **options):

#filename=str(settings.LOGFILES_DIR/splitext(__file__)[0]) + '.log'

        fff = settings.LOGFILES_DIR /(splitext(__file__)[0] + '.log')
        print('\n\n', fff) #settings.LOGFILES_DIR /(splitext(basename(__file__))[0] + '.log'), '\n\n')

        logging.error('aaaaaa')
        logging.info('do_actions запустился')
        GPIO.setmode(GPIO.BCM)
        while True:
            time.sleep(0.5)
            self.check_next_day
            self.check_end_tasks(self.end_tasks)
            for action in Action.objects.filter(done='in progress', pk__gt=self.last_task):
                logging.info('Новый Action.')
                self.activate(action.plant.numb, action.time, action)
                self.last_task=action.pk
            self.check_plant_time(Plant)



logging.basicConfig(filename=settings.LOGFILES_DIR /(splitext(__file__)[0] + '.log'),
                    level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
