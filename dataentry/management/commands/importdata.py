import csv
from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student,Customer
from django.apps import apps

# Proposed command: python manage.py inportdata file_path

class Command(BaseCommand):
    help= "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help='Path to the CSV file')
        parser.add_argument('model_name',type=str, help='Name of the model')
        
    def handle(self, *args,**kwargs):
        # Logic goes here 
        file_path= kwargs['file_path']
        model_name= kwargs['model_name'].capitalize()

# Searching for the models accross all installed Apps.
        model= None
        for app_config in apps.get_app_configs():
            try:
                model =apps.get_model(app_config.label,model_name)
                break # Stop searching once the model is found
            except LookupError:
                continue # model not found in this app, continue searching other apps.

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any apps.')

        with open(file_path,'r') as file:
            reader= csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV Successfully!'))

