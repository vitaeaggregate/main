from ..models.header import Header
from django.db import models

class Interest(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    name = models.CharField(blank=False)
    description = models.TextField(blank=True)