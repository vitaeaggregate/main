from rest_framework import serializers
from ..models.comment import Comment
from api.member.models.comment_notification import CommentNotification


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        out_data = {
            "id": instance.id,
            "member": instance.member.id,
            "header_info": {
                "id": instance.header.id,
                "title": instance.header.title,
            },
            "description": instance.description,
            "created_at": instance.created_at,
            "can_delete": False
        }

        request = self.context.get("request")

        member_id = request.account.get("id")

        if instance.header.member.id == member_id or instance.member.id == member_id:
            out_data["can_delete"] = True

        return out_data

    def create(self, validated_data):
        comment = super().create(validated_data)
        self.create_notification(comment, validated_data)

        return comment

    def create_notification(self, comment, validated_data):
        request = self.context.get("request")
        sender_id = request.account.get("id")
        receiver = validated_data.get("header").member

        if request.account.get("id") == receiver.id:
            return

        CommentNotification.objects.create(
            comment=comment, receiver=receiver, sender_id=sender_id)
