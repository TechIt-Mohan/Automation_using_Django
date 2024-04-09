from typing import Any
from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'It will insert the data.'

    def handle(self, *args, **kwargs):
        # Here we will write the business logic to insert data. 
        
        dataset =[        
            {'roll_no': 1009, 'name':"Jaadu",'age':20},
             {'roll_no': 1006, 'name':"Royal",'age':22},
             {'roll_no': 10010, 'name':"Paadu",'age':23},
             {'roll_no': 1007, 'name':"Carlos",'age':25},
    ]  
               
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists!'))
            self.stdout.write(self.style.SUCCESS(f'Student data inserted successfully!'))