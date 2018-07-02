from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# create your models here.
class D01_GeneralDetails(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    lsgd_name = models.CharField(max_length = 100)
    lsgd_year_of_formation = models.IntegerField()
    lsgd_area_in_sqkm = models.FloatField()

