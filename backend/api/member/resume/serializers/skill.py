from rest_framework import serializers
from ..models.skill import Skill


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Skill
        exclude = ["header"]
