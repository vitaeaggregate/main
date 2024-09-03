from rest_framework import viewsets
from ..models.award import Award
from ..serializers.award import AwardSerializer


class AwardViewSet(viewsets.ModelViewSet):
    serializer_class = AwardSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return Award.objects.filter(header_id=header_pk)
        return Award.objects.all()
