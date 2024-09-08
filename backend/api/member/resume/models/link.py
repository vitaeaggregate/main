from .header import Header
from django.db import models


class Link(models.Model):
    header = models.ForeignKey(Header, related_name="links", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=200, blank=False)
