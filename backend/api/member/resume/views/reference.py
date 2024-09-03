from rest_framework import viewsets
from ..models.reference import Reference
from ..serializers.reference import ReferenceSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if (header_pk):
            return Reference.objects.filter(header_id=header_pk)
        return Reference.objects.all()
