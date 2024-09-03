from ..models.header import Header
from django.db import models


class Course(models.Model):
    header = models.ForeignKey(
        Header, related_name="courses", on_delete=models.CASCADE, blank=False)
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
