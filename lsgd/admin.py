from __future__ import unicode_literals

from django.contrib import admin

from .models import District

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display=('district_code','district_name')


admin.site.register(District,DistrictAdmin)
