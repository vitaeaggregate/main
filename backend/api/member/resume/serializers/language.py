from rest_framework import serializers
from ..models.language import Language


class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Language
        exclude = ["header"]
