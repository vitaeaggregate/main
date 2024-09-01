from ..models.header import Header
from django.db import models


class Reference(models.Model):
    resume = models.ForeignKey(Header, related_name="references", on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    job_title = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
