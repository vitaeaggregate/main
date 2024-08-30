from ..models.header import Header
from django.db import models


class ProfessionalExp(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    job_title = models.CharField(blank=False)
    employer = models.CharField(blank=False)
    city = models.CharField(blank=True)
    country = models.CharField(blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField(blank=False)
