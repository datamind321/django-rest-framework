from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=28)
    email = models.CharField(max_length=28)
    city = models.CharField(max_length=28)
