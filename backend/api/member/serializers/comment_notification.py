from rest_framework import serializers
from ..models.comment_notification import CommentNotification


class CommentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentNotification
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "is_read": instance.is_read,
            "comment": {
                "id": instance.comment.id,
                "description": instance.comment.description
            },
            "header": {
                "id": instance.comment.header.id,
                "title": instance.comment.header.title
            },
            "created_at": instance.created_at
        }