from api.member.models.account import Account
from django.db import models


class Header(models.Model):
    member = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=False)
    title = models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
