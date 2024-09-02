from django.db import models
from api.member.models.account import Account
from django.conf import settings

class CustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    account = models.OneToOneField(Account, related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)