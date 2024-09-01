from ..models.header import Header
from django.db import models


class ProfessionalExp(models.Model):
    resume = models.ForeignKey(Header, related_name="professional_exps", on_delete=models.CASCADE, blank=False)
    job_title = models.CharField(max_length=100, blank=False)
    employer = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=False)
