from __future__ import unicode_literals

from django.contrib import admin
from data.models import D01_GeneralDetails

# Register your models here.
class D01_GeneralDetailsAdmin(admin.ModelAdmin):
    list_display = ('lsgd_code_and_year', 'lsgd_name','lsgd_year_of_formation','lsgd_area_in_sqkm','lsgd_no_of_wards','lsgd_taluk_name')

admin.site.register(D01_GeneralDetails, D01_GeneralDetailsAdmin)
