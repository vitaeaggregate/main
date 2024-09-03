from ..models.header import Header
from django.db import models


class Project(models.Model):
    header = models.ForeignKey(Header, related_name="projects", on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=100, blank=False)
    sub_title = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=False)
