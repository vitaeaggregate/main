from enum import Enum
from django.http import JsonResponse
from rest_framework import viewsets

from api.member.models.account import Account
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

        comments = Comment.objects.all()

        if header_pk:
            try:
                header = Header.objects.get(id=header_pk)
            except header.DoesNotExist():
                return JsonResponse({"detail": "Resume not found."}, status=404)

            comments = comments.filter(header_id=header_pk)

        elif member_pk:
            try:
                member = Account.objects.get(id=member_pk)
            except member.DoesNotExist():
                return JsonResponse({"detail": "Member not found."}, status=404)

            comments = comments.filter(member_id=member_pk)

        return comments

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.is_owner(request, Action.UPDATE):
            return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.is_owner(request, Action.DELETE):
            return super().destroy(request, *args, **kwargs)

    def is_owner(self, request, action: Action) -> bool:
        member_id = request.account.get("id")
        header_owner = self.get_object().header.member.id
        if member_id not in [self.get_object().member.id, header_owner]:
            raise PermissionDenied(
                "You Don't have the permission to " + action.__str__() + " a comment in the name of another user.")
        return True
