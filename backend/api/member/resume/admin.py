from django.contrib import admin
from .models.header import Header
from .models.comment import Comment

admin.site.register(Header)
admin.site.register(Comment)