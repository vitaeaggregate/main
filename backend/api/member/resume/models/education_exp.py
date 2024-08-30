from ..models.header import Header
from django.db import models


class EducationExp(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    degree = models.CharField(blank=True)
    institution = models.CharField(blank=True)
    city = models.CharField(blank=True)
    country = models.CharField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(blank=True)
