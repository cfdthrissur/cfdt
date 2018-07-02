from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# create your models here.
class D01_GeneralDetails(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    lsgd_name = models.CharField(max_length = 100, unique = True)
    lsgd_year_of_formation = models.IntegerField(null = True)
    lsgd_area_in_sqkm = models.FloatField(null = True)
    lsgd_taluk_name = models.CharField(max_length = 100, null = True)
    lsgd_block_name = models.CharField(max_length = 100, null = True)
    lsgd_parliamentary_constituency = models.CharField(max_length = 100, null = True) 
    lsgd_assembly_constituency = models.CharField(max_length = 100, null = True)
    lsgd_no_of_wards = models.IntegerField(null = True)
    lsgd_no_of_female_wards = models.IntegerField(null = True)
    lsgd_no_of_scst_wards = models.IntegerField(null = True)
