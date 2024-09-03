from ..models.header import Header
from ...models.account import Account
from django.db import models


class Comment(models.Model):
    header = models.ForeignKey(
        Header, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(
        Account, related_name="comments", on_delete=models.SET_NULL, blank=False, null=True)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
