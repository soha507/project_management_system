from django.db import models
from django.db import models
from unittest.util import _MAX_LENGTH
import datetime
from django.core.exceptions import ValidationError


class appointment(models.Model):
    username=models.CharField
    hospitalname = models.CharField(max_length=200)
    specialistname = models.CharField(max_length=200)
    pname = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
def str(self):
    return ' Name : ' + self.hname + ' - Date : ' + self.hdate

class contact(models.Model):
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)




