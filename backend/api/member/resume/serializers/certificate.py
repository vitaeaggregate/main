from rest_framework import serializers
from ..models.certificate import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Certificate
        exclude = ["header"]
