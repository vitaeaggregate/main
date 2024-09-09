from rest_framework import serializers
from ..models.education import Education


class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Education
        exclude = ["header"]
