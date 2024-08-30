from rest_framework import viewsets
from ..models.skill import Skill
from ..serializers.skill import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if(resume_pk):
            return Skill.objects.filter(resume_id=resume_pk)
        return Skill.objects.all()