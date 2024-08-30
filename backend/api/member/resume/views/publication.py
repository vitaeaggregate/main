from rest_framework import viewsets
from ..models.publication import Publication
from ..serializers.publication import PublicationSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if(resume_pk):
            return Publication.objects.filter(resume_id=resume_pk)
        return Publication.objects.all()