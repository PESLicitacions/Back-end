# myapp/management/commands/my_command.py
from django.core.management.base import BaseCommand
from publicdata.views import get_data

class Command(BaseCommand):
    help = 'Fetches public data'

    def handle(self, *args, **options):
        get_data()
