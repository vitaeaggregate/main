from enum import Enum
from django.http import JsonResponse
from rest_framework import viewsets
from ..models.comment import Comment
from ..models.comment import Header
from ..serializers.comment import CommentSerializer
from rest_framework.exceptions import PermissionDenied


class Action(Enum):
    DELETE = "DELETE"
    UPDATE = "UPDATE"
    CREATE = "CREATE"


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        member_pk = self.kwargs.get("member_pk")

        if header_pk:
            try:
                header = Header.objects.get(id=header_pk)
            except header.DoesNotExist():
                return JsonResponse({"detail": "Resume not found."}, status=404)

            comments = Comment.objects.filter(header_id=header_pk)

        else:
            comments = []
            comments_filter = Comment.objects.filter(member_id=member_pk)
            for comment in comments_filter:
                if comment.header.is_shareable or self.request.account.get("id") == comment.member.id:
                    comments.append(comment)

        return comments

    def create(self, request, *args, **kwargs):
        if self.is_owner(request, Action.CREATE):
            return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.is_owner(request, Action.UPDATE):
            return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.is_owner(request, Action.DELETE):
            return super().destroy(request, *args, **kwargs)

    def is_owner(self, request, action: Action) -> bool:
        member_pk = self.kwargs.get("member_pk")
        if not int(member_pk) == request.account.get("id"):
            raise PermissionDenied(
                "You Don't have the permission to " + action.__str__() + " a resume in the name of another user.")
        return True
