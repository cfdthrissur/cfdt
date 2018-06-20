from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class District(models.Model):
    district_code = models.CharField(max_length = 10, unique = True, primary_key=True)
    district_name = models.CharField(max_length = 50, unique = True)
   
class Lsgd(models.Model):
    lsgd_code = models.CharField(max_length = 15, unique = True, primary_key = True)
    lsgd_name = models.CharField(max_length = 100, unique = True)
    lsgd_type = models.CharField(max_length = 15)
