from ..models.header import Header
from django.db import models


class Certificate(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    name = models.CharField(blank=True)
    description = models.TextField(blank=True)
