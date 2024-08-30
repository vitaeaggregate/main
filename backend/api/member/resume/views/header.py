from rest_framework import viewsets
from ..models.header import Header
from ..serializers.header import HeaderSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    serializer_class = HeaderSerializer

    def get_queryset(self):
        member_pk = self.kwargs.get('member_pk')        
        if member_pk:
            return Header.objects.filter(member_id=member_pk)
        return Header.objects.all()