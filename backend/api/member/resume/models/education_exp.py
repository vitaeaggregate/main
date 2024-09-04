from ..models.header import Header
from django.db import models


class EducationExp(models.Model):
    header = models.ForeignKey(Header, related_name="educations_exps", on_delete=models.CASCADE, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
