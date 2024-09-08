from rest_framework import viewsets
from ..models.publication import Publication
from ..serializers.publication import PublicationSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if(header_pk):
            return Publication.objects.filter(header_id=header_pk)
        return Publication.objects.all()