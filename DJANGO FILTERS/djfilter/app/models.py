from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=28)
    email = models.CharField(max_length=28)
    city = models.CharField(max_length=28)
    passby = models.CharField(max_length=20)
