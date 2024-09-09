from rest_framework import serializers
from ..models.award import Award


class AwardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Award
        exclude = ["header"]
