from rest_framework import viewsets
from ..models.link import Link
from ..serializers.link import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if (header_pk):
            return Link.objects.filter(header_id=header_pk)
        return Link.objects.all()
