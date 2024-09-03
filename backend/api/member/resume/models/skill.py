from ..models.header import Header
from django.db import models


class Skill(models.Model):
    header = models.ForeignKey(Header, related_name="skills", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    skill_level = models.CharField(max_length=50, blank=True)
