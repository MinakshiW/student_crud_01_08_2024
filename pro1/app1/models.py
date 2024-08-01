from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=34)
    marks = models.IntegerField()
    gender = models.CharField(max_length=23)
    city = models.CharField(max_length=23)