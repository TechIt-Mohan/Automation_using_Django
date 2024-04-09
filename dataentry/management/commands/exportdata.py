import csv, datetime
from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser
from dataentry.models import Student, Customer


# Proposed command = python manage.py exportdata from a model.
#
#class Command(BaseCommand):
#    help = 'Export data from Student model to CSV file'
#
#    def handle(self, *args, **kwargs):
#    # Logic for fetching the file and writing.
#    
#        #Fetch the data from the database
#        students= Student.objects.all()
#
#        # Generate the time-stamp of export file date and time;
#        timestamp= datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#        #define the CSV file name/path
#        file_path = f'exported_students_data_{timestamp}.csv'
#
#        #Open the csv file and write the data 
#        with open(file_path, 'w', newline='') as file:
#            writer= csv.writer(file)
#
#            # Write the CSV header 
#            writer.writerow(['Roll No', 'Name', 'Age'])
#
#            # Write datarows
#            for student in students:
#                writer.writerow([student.roll_no, student.name, student.age])
#
#        #self.stdout.write(self.style.SUCCESS('Data exported Successfully'))
#        self.stdout.write(self.style.SUCCESS('Data exported Successfully'))

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
##??????????????????????????????????????????????????????????????????????????????????????????????????????????##
##//////////////////////////////////////////////////////////////////////////////////////////////////////////##


# Proposed program for exporting data from multiple models in different formats like, csv, pdf, yml, html:

class Command(BaseCommand):
    help = 'Export data from Student model to CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name',type=str, help='Model name')

    def handle(self, *args, **kwargs):
        model_name= kwargs['model_name']

# Search through all the installed apps for the model.
        model = None
        for app_config in apps.get_app_configs():

            try:  #Looping through the models here
                model = apps.get_model(app_config.label, model_name)
                break # Stop once the model in found in an / any apps that are installed.
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'Model {model_name} could not be found')
            return 
            
        #Fetch the data from the database. 
        data = model.objects.all() 

        # Generate the time-stamp of export file date and time;
        timestamp= datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        #define the CSV file name/path
        file_path = f'exported_data_{timestamp}.csv'

        #Open the csv file and write the data 
        with open(file_path, 'w', newline='') as file:
            writer= csv.writer(file)

            # Write the CSV header using the List comprehenssion method  
            # We want to print the field names of the model that we are trying to export 
            writer.writerow([ field.name for field in model._meta.fields])

            # Writin the rows, menas the data of any model and looking through all the data.
            for dt in data:
                writer.writerow([getattr (dt, field.name)for field in model._meta.fields])

        #self.stdout.write(self.style.SUCCESS('Data exported Successfully'))
        self.stdout.write(self.style.SUCCESS('Data exported Successfully'))


