# forms.py
from django import forms
from .models import CourtCase

class CourtCaseForm(forms.ModelForm):
    class Meta:
        model = CourtCase
        fields = ['case_number', 'judge_name', 'case_type', 'filing_date']
