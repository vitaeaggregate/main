from rest_framework import serializers
from ..models.interest import Interest


class InterestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Interest
        exclude = ["header"]
