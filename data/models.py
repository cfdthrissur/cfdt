from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# create your models here.
# Genearl Details of LSGD
class D001(models.Model):
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
    lsgd_no_of_rivers = models.IntegerField(null = True)
    lsgd_name_of_rivers = models.TextField(null = True)
    lsgd_coastal_line_length_in_km = models.FloatField(null = True)
    lsgd_forest_area_in_hectors = models.FloatField(null = True)
    lsgd_type_of_soil = models.CharField(max_length = 100, null = True)
    lsgd_main_roads = models.TextField(null = True)
    lsgd_nearest_railway_station = models.CharField(max_length = 100, null = True)
    lsgd_jilla_panchayath_name = models.CharField(max_length = 100, null = True)
    lsgd_jilla_panchayath_ward = models.IntegerField(null = True)
    lsgd_block_panchayath_name = models.CharField(max_length = 100, null = True)
    lsgd_block_panchayath_wards = models.CharField(max_length = 100, null = True)

# Demographic particulars of LSGD
class D002(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    population_male = models.IntegerField(null = True)
    population_female = models.IntegerField(null = True)
    population_male_sc = models.IntegerField(null = True)
    population_female_sc = models.IntegerField(null = True)
    population_male_st = models.IntegerField(null = True)
    population_female_st = models.IntegerField(null = True)
    children_0_to_6_age_male = models.IntegerField(null = True)
    children_0_to_6_age_female = models.IntegerField(null = True)
    children_0_to_6_age_male_sc = models.IntegerField(null = True)
    children_0_to_6_age_female_sc = models.IntegerField(null = True)
    children_0_to_6_age_male_st = models.IntegerField(null = True)
    children_0_to_6_age_female_st = models.IntegerField(null = True)
    children_6_to_10_age_male = models.IntegerField(null = True)
    children_6_to_10_age_female = models.IntegerField(null = True)
    children_0_to_18_age_male = models.IntegerField(null = True)
    children_0_to_18_age_female = models.IntegerField(null = True)
    literates_male = models.IntegerField(null = True)
    literates_female = models.IntegerField(null = True)
    migrant_labours_male = models.IntegerField(null = True)
    migrant_labours_female = models.IntegerField(null = True)
    migrant_labours_child_male = models.IntegerField(null = True)
    migrant_labours_child_female = models.IntegerField(null = True)
    third_gender_persons = models.IntegerField(null = True)
    household_all = models.IntegerField(null = True)
    household_sc = models.IntegerField(null = True)
    household_st = models.IntegerField(null = True)
    bpl_families = models.IntegerField(null = True)

# Sex Desegregated Data of Children
class D003(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    children_male_below_age_1 = models.IntegerField(null = True)
    children_female_below_age_1 = models.IntegerField(null = True)
    children_male_1_to_3_age = models.IntegerField(null = True)
    children_female_1_to_3_age = models.IntegerField(null = True)
    children_male_3_to_5_age = models.IntegerField(null = True)
    children_female_3_to_5_age = models.IntegerField(null = True)
    children_male_5_to_6_age = models.IntegerField(null = True)
    children_female_5_to_6_age = models.IntegerField(null = True)
    children_male_6_to_10_age = models.IntegerField(null = True)
    children_female_6_to_10_age = models.IntegerField(null = True)
    children_male_10_to_18_age = models.IntegerField(null = True)
    children_female_10_to_18_age = models.IntegerField(null = True)

