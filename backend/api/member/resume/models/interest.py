from ..models.header import Header
from django.db import models


class Interest(models.Model):
    header = models.ForeignKey(Header, related_name="interests", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
