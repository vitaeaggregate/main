from rest_framework import serializers
from ..models.comment import Comment
from api.member.models.comment_notification import CommentNotification


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "header": {
                "id": instance.header.id,
                "title": instance.header.title,
            },
            "description": instance.description,
            "created_at": instance.created_at
        }

    def create(self, validated_data):
        comment = super().create(validated_data)

        sender = validated_data.get("member")
        receiver = validated_data.get("header").member

        CommentNotification.objects.create(
            comment=comment, receiver=receiver, sender=sender)

        return comment
