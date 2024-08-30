from rest_framework import viewsets
from ..models.interest import Interest
from ..serializers.interest import InterestSerializer


class InterestViewSet(viewsets.ModelViewSet):
    serializer_class = InterestSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if (resume_pk):
            return Interest.objects.filter(resume_id=resume_pk)
        return Interest.objects.all()
