from rest_framework import serializers
from ..models.reference import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Reference
        exclude = ["header"]
