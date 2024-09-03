from django.db import models
from .header import Header


class Award(models.Model):
    header = models.ForeignKey(
        Header, related_name="awards", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True)
    issuer = models.CharField(max_length=100, blank=True)
    date = models.DateField(null=True)
    description = models.TextField(blank=True)
