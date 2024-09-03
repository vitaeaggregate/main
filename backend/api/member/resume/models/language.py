from ..models.header import Header
from django.db import models

class Language(models.Model):
    header = models.ForeignKey(Header, related_name="languages", on_delete=models.CASCADE, blank=False)
    language = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    skill_level = models.CharField(max_length=100, blank=False)
