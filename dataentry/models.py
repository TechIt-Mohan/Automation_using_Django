from django.db import models

# Create your models 

class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name= models.CharField(max_length=35)
    country= models.CharField(max_length=25)
   
    def __str__(self):
        return self.customer_name
    
    