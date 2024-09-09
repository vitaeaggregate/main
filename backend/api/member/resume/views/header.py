from enum import Enum
import json
from django.http import JsonResponse
from rest_framework import viewsets, status
from ..models.header import Header
from ..serializers.header import HeaderSerializer
from rest_framework.exceptions import PermissionDenied


class Action(Enum):
    DELETE = "DELETE"
    UPDATE = "UPDATE"
    CREATE = "CREATE"


class HeaderViewSet(viewsets.ModelViewSet):
    serializer_class = HeaderSerializer

    def get_queryset(self):
        member_pk = self.kwargs.get("member_pk")
        if member_pk:
            return Header.objects.filter(member_id=member_pk)
        return Header.objects.filter(is_shareable=True)

    def create(self, request, *args, **kwargs):
        if self.is_owner(request, Action.CREATE):
            return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if self.is_owner(request, Action.UPDATE):
            for key in request.data:
                if isinstance(request.data[key], list):
                    for item in request.data[key]:
                        if not isinstance(item.get("id"), int):
                            item.pop("id")

            return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.is_owner(request, Action.DELETE):
            return super().destroy(request, *args, **kwargs)

    def is_owner(self, request, action: Action) -> bool:
        member_pk = self.kwargs.get("member_pk")
        if not int(member_pk) == request.account.get("id"):
            raise PermissionDenied(
                "You Don't have the permission to " + action.__str__() + " a resume in the name of another user.")
        return True
