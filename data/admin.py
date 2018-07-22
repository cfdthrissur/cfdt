from __future__ import unicode_literals

from django.contrib import admin
from data.models import D001, D002

# Register your models here.
class D001Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'lsgd_name','lsgd_year_of_formation','lsgd_area_in_sqkm','lsgd_no_of_wards','lsgd_taluk_name','lsgd_block_panchayath_wards')

class D002Admin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'population_male', 'population_female')

admin.site.register(D001, D001Admin)
admin.site.register(D002, D002Admin)

