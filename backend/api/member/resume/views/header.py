from rest_framework import viewsets
from django.db.models import Q
from ..models.header import Header
from ..serializers.header import HeaderSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    serializer_class = HeaderSerializer

    def get_queryset(self):
        member_pk = self.kwargs.get("member_pk")
        if member_pk:
            # account = self.request.account
            account = {
                "id": 15
            }

            return Header.objects.filter(member_id=member_pk)
        return Header.objects.all()
