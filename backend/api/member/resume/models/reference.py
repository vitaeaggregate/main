from ..models.header import Header
from django.db import models


class Reference(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    name = models.CharField(blank=False)
    job_title = models.CharField(blank=True)
    organization = models.CharField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True)
