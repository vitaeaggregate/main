from ..models.header import Header
from django.db import models


class Project(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    title = models.CharField(blank=False)
    sub_title = models.CharField(blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField(blank=False)
