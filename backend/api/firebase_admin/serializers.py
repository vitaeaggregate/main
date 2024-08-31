from rest_framework import serializers
from api.member.models.account import Account

class FirebaseAccountSerializer(serializers.ModelSerializer):
    firebase_token = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = "__all__"