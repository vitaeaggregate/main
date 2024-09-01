from ..models.header import Header
from django.db import models


class Publication(models.Model):
    resume = models.ForeignKey(Header, related_name="publications", on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=200, blank=False)
    publisher = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
