from __future__ import unicode_literals

import datetime

from django.db import models

class UserPhoto(models.Model):
    user_name = models.CharField(max_length=128, default="")
    user_phone = models.CharField(max_length=128, default="")
    access_code = models.CharField(max_length=128)
    photo_name = models.CharField(max_length=128)

class Appointment(models.Model):
    user_name = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    user_email = models.CharField(max_length=32)
    #submit_time = models.DateTimeField(default=datetime.datetime.now)
    #finish_time = models.DateTimeField(default=datetime.datetime.now, blank=True)

class AvailableTime(models.Model):
    #day = models.DateTimeField(default=datetime.datetime.now)
    time1 = models.IntegerField(default=0)
    time2 = models.IntegerField(default=0)
    time3 = models.IntegerField(default=0)
    time4 = models.IntegerField(default=0)
    time5 = models.IntegerField(default=0)
    time6 = models.IntegerField(default=0)
    time7 = models.IntegerField(default=0)
    time8 = models.IntegerField(default=0)
