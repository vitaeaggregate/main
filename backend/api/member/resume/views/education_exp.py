from rest_framework import viewsets
from ..models.education_exp import EducationExp
from ..serializers.education_exp import EducationExpSerializer


class EducationExpViewSet(viewsets.ModelViewSet):
    serializer_class = EducationExpSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            return EducationExp.objects.filter(resume_id=resume_pk)
        return EducationExp.objects.all()
