from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    city = models.CharField(max_length=25)