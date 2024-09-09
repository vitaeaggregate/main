from rest_framework import serializers
from ..models.link import Link


class LinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Link
        exclude = ["header"]
