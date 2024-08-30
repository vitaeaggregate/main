from rest_framework import serializers
from ..models.professional_exp import ProfessionalExp


class ProfessionalExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExp
        fields = "__all__"
