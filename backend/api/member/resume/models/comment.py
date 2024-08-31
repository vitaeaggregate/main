from ..models.header import Header
from ...models.account import Account
from django.db import models


class Comment(models.Model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    member = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False)
    description = models.CharField(blank=False)
