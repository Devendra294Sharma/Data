from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=40)
    City = models.CharField(max_length=40)
    Country = models.CharField(max_length=40)
    Roll = models.IntegerField()