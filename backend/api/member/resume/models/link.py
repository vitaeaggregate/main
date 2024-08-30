from .header import Header
from django.db import models

class Link(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    title = models.CharField(blank=False)
    url = models.CharField(blank=False)