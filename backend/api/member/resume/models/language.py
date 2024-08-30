from ..models.header import Header
from django.db import models


class Language(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    language = models.CharField(blank=False)
    description = models.TextField(blank=False)
    skill_level = models.CharField(blank=False)
