from enum import Enum
from django.http import JsonResponse
from rest_framework import viewsets, status
from ..models.header import Header
from ..serializers.header import HeaderSerializer
from rest_framework.exceptions import PermissionDenied
from django.db import models


class Action(Enum):
    DELETE = "DELETE"
    UPDATE = "UPDATE"


class HeaderViewSet(viewsets.ModelViewSet):
    serializer_class = HeaderSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("pk")
        member_pk = self.kwargs.get("member_pk")
        member_id = self.request.account.get("id")

        resumes = Header.objects.all()

        resumes = resumes.filter(
            models.Q(is_shareable=True) | models.Q(member_id=member_id))

        if member_pk:
            resumes = resumes.filter(member_id=member_id)

        return resumes

    def create(self, request, *args, **kwargs):
        self.remove_id(request)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if self.is_owner(request, Action.UPDATE):
            self.remove_id(request)
            return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.is_owner(request, Action.DELETE):
            return super().destroy(request, *args, **kwargs)

    def is_owner(self, request, action: Action) -> bool:
        member_id = request.account.get("id")
        if not member_id == self.get_object().member.id:
            raise PermissionDenied(
                "You Don't have the permission to " + action.__str__() + " a resume in the name of another user.")
        return True

    def remove_id(self, request):
        for key in request.data:
            if isinstance(request.data[key], list):
                for item in request.data[key]:
                    if not isinstance(item.get("id"), int):
                        item.pop("id")
