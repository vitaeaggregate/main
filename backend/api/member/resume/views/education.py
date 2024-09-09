from rest_framework import viewsets
from ..models.education import EducationExp
from ..serializers.education import EducationSerializer


class EducationExpViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return EducationExp.objects.filter(header_id=header_pk)
        return EducationExp.objects.all()
