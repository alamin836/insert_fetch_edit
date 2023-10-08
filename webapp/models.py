from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
    
