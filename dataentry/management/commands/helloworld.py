from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):

        # In this method or Fundtion we write our business logic
        
        self.stdout.write('HelloWorld')