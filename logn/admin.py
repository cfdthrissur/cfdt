from __future__ import unicode_literals

from django.contrib import admin
from logn.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_lsgd','user_type')

admin.site.register(Profile, ProfileAdmin)
