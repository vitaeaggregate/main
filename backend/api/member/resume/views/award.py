from rest_framework import viewsets
from ..models.award import Award
from ..serializers.award import AwardSerializer


class AwardViewSet(viewsets.ModelViewSet):
    serializer_class = AwardSerializer

    def get_queryset(self):
        resume_pk = self.kwards.get('resume_pk')
        if resume_pk:
            return Award.objects.filter(resume_id=resume_pk)
        return Award.objects.all()
