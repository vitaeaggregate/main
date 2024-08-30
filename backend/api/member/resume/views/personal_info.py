from rest_framework import viewsets
from ..models.personal_info import PersonalInfo
from .. serializers.personal_info import PersonalInfoSerializer


class PersonalInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalInfoSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if (resume_pk):
            return PersonalInfo.objects.filter(resume_id=resume_pk)
        return PersonalInfo.objects.all()
