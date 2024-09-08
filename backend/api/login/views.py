from uuid import uuid4
from rest_framework.views import APIView
from django.http import JsonResponse
from api.member.models.account import Account
from api.member.serializers.account import AccountSerializer
from .models import CustomToken
from rest_framework import status


class DjangoSessionApiView(APIView):
    def post(self, request):
        email = request.data.get("email")

        try:
            account = Account.objects.get(email=email)
            
            token_key = str(uuid4())

            token, created = CustomToken.objects.get_or_create(account=account, defaults={"key": token_key})

            account_serializer = AccountSerializer(account)

            return JsonResponse({"token": token.key, "account": account_serializer.data}, status=status.HTTP_200_OK)

        except Account.DoesNotExist:
            return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            token_key = request.headers.get("Authorization")

            token = CustomToken.objects.filter(key=token_key).first()
            if token:
                token.delete()
                return JsonResponse({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "Wrong token or not provided"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return JsonResponse({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
