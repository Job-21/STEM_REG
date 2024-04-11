from django.db import models

# Create your models here.

class StudentsData(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
