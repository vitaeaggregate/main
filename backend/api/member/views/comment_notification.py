from rest_framework import viewsets
from ..models.comment_notification import CommentNotification
from ..serializers.comment_notification import CommentNotificationSerializer


class CommentNotificationViewSet(viewsets.ModelViewSet):
    serializer_class = CommentNotificationSerializer

    def get_queryset(self):
        receiver_pk = self.kwargs.get("member_pk")
        is_read = self.request.query_params.get("is_read")
        if receiver_pk:
            notifications = CommentNotification.objects.filter(
                receiver_id=receiver_pk).order_by("-created_at")
            if is_read == "false":
                notifications = notifications.filter(is_read=False)
            return notifications
        return CommentNotification.objects.all()
