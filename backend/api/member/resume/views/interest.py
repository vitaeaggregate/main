from rest_framework import viewsets
from ..models.interest import Interest
from ..serializers.interest import InterestSerializer


class InterestViewSet(viewsets.ModelViewSet):
    serializer_class = InterestSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if (header_pk):
            return Interest.objects.filter(header_id=header_pk)
        return Interest.objects.all()
