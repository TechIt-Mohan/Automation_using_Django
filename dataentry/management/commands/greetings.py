from typing import Any
from django.core.management.base import BaseCommand, CommandParser



#Proposed Commmand = paython manage.py greeting name
#Proposed Output = Hi {name} Good Morning!

class Command(BaseCommand):
    help = "Greet the User" # help - This is command level help text 

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies UserName") # help- This is argument level help text

    def handle(self, *args: Any, **kwargs):
        name = kwargs['name']
        greeting = f'hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))
