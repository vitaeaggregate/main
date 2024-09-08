from api.member.models.account import Account
from django.db import models


class Header(models.Model):
    member = models.ForeignKey(
        Account, related_name="headers", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False)
    is_shareable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)