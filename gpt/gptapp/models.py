# models.py
from django.db import models

class CourtCase(models.Model):
    case_number = models.CharField(max_length=100)
    judge_name = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100)
    filing_date = models.DateField()

    def __str__(self):
        return self.case_number
