from rest_framework import serializers
from ..models.award import Award


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"
