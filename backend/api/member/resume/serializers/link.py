from rest_framework import serializers
from ..models.link import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
