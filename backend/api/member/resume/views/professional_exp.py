from rest_framework import viewsets
from ..models.professional_exp import ProfessionalExp
from ..serializers.professional_exp import ProfessionalExpSerializer


class ProfessionalExpViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionalExpSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if member_pk:
            return ProfessionalExp.objects.filter(member_id=resume_pk)
        return ProfessionalExp.objects.all()
