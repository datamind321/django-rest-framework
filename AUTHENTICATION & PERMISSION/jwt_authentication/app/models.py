from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=27)
    email = models.CharField(max_length=27)
    city = models.CharField(max_length=27)