from django.contrib import admin

# Register your models here.
from gptapp.models import CourtCase
class adminji(admin.ModelAdmin):
    list_display=( 'case_number','judge_name','case_type','filing_date' )

admin.site.register(CourtCase,adminji)