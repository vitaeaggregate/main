from ..models.header import Header
from django.db import models


class Certificate(models.Model):
    resume = models.ForeignKey(
        Header, related_name="certificates", on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
