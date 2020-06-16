# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=30)
    duration = models.IntegerField()
    expire_date = models.DateField(default=datetime.date.today())
    description = models.CharField(max_length=1000)
