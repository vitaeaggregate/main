from ..models.header import Header
from django.db import models


class Award(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    title = models.CharField(blank=True)
    issuer = models.CharField(blank=True)
    date = models.DateField(null=True)
    description = models.TextField(blank=True)
