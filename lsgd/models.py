from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class district(models.Model):
    district_code=models.CharField(max_length=10,unique=True)
    district_name=models.CharField(max_length=50,unique=True)