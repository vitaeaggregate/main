from rest_framework import viewsets
from ..models.personal_info import PersonalInfo
from ..serializers.personal_info import PersonalInfoSerializer


class PersonalInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalInfoSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if (header_pk):
            return PersonalInfo.objects.filter(header_id=header_pk)
        return PersonalInfo.objects.all()
