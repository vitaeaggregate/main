from rest_framework import serializers
from ..models.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "can_comment",
            "created_at",
            "updated_at",
        ]
