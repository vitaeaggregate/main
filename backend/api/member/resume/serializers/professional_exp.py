from rest_framework import serializers
from ..models.professional_exp import ProfessionalExp


class ProfessionalExpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProfessionalExp
        exclude = ["header"]
