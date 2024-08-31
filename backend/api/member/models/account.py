from django.db import models


class Account(models.Model):
    email = models.EmailField(blank=False, unique=True)
    firebase_uid = models.CharField(blank=True, unique=True)
    can_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
