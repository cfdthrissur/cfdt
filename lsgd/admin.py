from __future__ import unicode_literals

from django.contrib import admin

from lsgd.models import District, Lsgd

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display=('district_code', 'district_name')

class LsgdAdmin(admin.ModelAdmin):
    list_display=('lsgd_code', 'lsgd_name', 'lsgd_type')


admin.site.register(District, DistrictAdmin)
admin.site.register(Lsgd, LsgdAdmin)
