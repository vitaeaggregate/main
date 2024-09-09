from rest_framework import serializers
from ..models.publication import Publication


class PublicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Publication
        exclude = ["header"]
