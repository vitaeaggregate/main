from django.contrib import admin
from .models.account import Account
from .models.comment_notification import CommentNotification

admin.site.register(Account)
admin.site.register(CommentNotification)