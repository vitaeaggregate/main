from .header import Header
from django.db import models


class Link(models.Model):
    resume = models.ForeignKey(Header, related_name="links", on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=200, blank=False)
