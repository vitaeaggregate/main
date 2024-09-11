from django.db import models
from api.member.resume.models.comment import Comment
from .account import Account


class CommentNotification(models.Model):
    sender = models.ForeignKey(
        Account, related_name="sent_notifications", on_delete=models.CASCADE, blank=True, null=True)
    receiver = models.ForeignKey(
        Account, related_name="received_notifications", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
