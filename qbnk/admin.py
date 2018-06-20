from __future__ import unicode_literals

from django.contrib import admin
from qbnk.models import QuestionBank

# Register your models here.
class QuestionBankAdmin(admin.ModelAdmin):
   list_display = ('question_code', 'question_text', 'question_type','question_options')

admin.site.register(QuestionBank, QuestionBankAdmin)
