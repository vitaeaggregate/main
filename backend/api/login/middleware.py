from api.member.serializers.account import AccountSerializer
from .models import CustomToken
from django.http import JsonResponse
from rest_framework import status


class DjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin") or request.path.startswith("/sessions"):
            return self.get_response(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JsonResponse({'status': 'error', 'message': 'Token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        auth_header = auth_header.split(" ")

        token_key = auth_header[1]

        if not token_key:
            return JsonResponse({'status': 'error', 'message': 'Token is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = CustomToken.objects.get(key=token_key,)

            request.account = AccountSerializer(token.account).data

            return self.get_response(request)

        except Exception as err:
            return JsonResponse({'status': 'error', 'message': 'Invalid token and/or wrong user'}, status=status.HTTP_401_UNAUTHORIZED)
