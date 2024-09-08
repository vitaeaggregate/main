from rest_framework import serializers
from ..models.personal_info import PersonalInfo


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"
