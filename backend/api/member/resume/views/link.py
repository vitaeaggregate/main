from rest_framework import viewsets
from ..models.link import Link
from ..serializers.link import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if (resume_pk):
            return Link.objects.filter(resume_id=resume_pk)
        return Link.objects.all()
