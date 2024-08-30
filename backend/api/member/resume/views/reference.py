from rest_framework import viewsets
from ..models.reference import Reference
from ..serializers.reference import ReferenceSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if (resume_pk):
            return Reference.objects.filter(resume_id=resume_pk)
        return Reference.objects.all()
