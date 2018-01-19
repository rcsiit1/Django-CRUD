from django.db import models
import datetime


class info(models.Model):
    firstname= models.CharField(max_length=250)
    lastname= models.CharField(max_length=250)
    designation= models.CharField(max_length=250,default='null')
    department= models.CharField(max_length=100,default='null')
    date=models.DateField()

    def __str__(self):
        return self.firstname

