from rest_framework import serializers
from ..models.education_exp import EducationExp


class EducationExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationExp
        fields = "__all__"
