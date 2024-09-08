from rest_framework import viewsets
from ..models.skill import Skill
from ..serializers.skill import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if(header_pk):
            return Skill.objects.filter(header_id=header_pk)
        return Skill.objects.all()