from rest_framework import viewsets
from ..models.professional_exp import ProfessionalExp
from ..serializers.professional_exp import ProfessionalExpSerializer


class ProfessionalExpViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionalExpSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return ProfessionalExp.objects.filter(header_id=header_pk)
        return ProfessionalExp.objects.all()
