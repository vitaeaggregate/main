from ..models.header import Header
from ...models.account import Account
from django.db import models


class Comment(models.Model):
    header = models.ForeignKey(
        Header, related_name="comments", on_delete=models.CASCADE, blank=False)
    member = models.ForeignKey(
        Account, related_name="comments", on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=False)
