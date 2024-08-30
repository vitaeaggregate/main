from rest_framework import serializers
from ..models.header import Header


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"
