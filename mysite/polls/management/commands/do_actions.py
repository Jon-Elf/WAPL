from django.core.management.base import BaseCommand, CommandError
from polls.models import Action, Plant
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            time.sleep(30)
            actions = Action.objects.
