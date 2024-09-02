from api.member.models.account import Account
from api.member.serializers.account import AccountSerializer

from django.http import JsonResponse
from rest_framework import status
from firebase_admin import auth
from .config import firebase_admin_app


class FirebaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin"):
            return self.get_response(request)

        auth_header = request.headers.get("Authorization")

        #TODO DELETE
        # auth_header = "a a"

        if not auth_header:
            return JsonResponse({'status': 'error', 'message': 'Authorization header missing'}, status=status.HTTP_401_UNAUTHORIZED)

        auth_header = auth_header.split(" ")
        firebase_token = auth_header[1]

        if not firebase_token:
            return JsonResponse({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decode_token = auth.verify_id_token(firebase_token)

            firebase_uid = decode_token["uid"]
            email = decode_token["email"]

            # TODO DELETE
            # firebase_uid = "I child leg probably others run other. Huge best join offer per."
            # email = auth_header[2]
            
            account, created = Account.objects.update_or_create(
                email=email,
                defaults={"firebase_uid": firebase_uid}
            )

            print("Hard coded user id: ", account.id)

            request.account = AccountSerializer(account).data

            return self.get_response(request)

        except auth.InvalidIdTokenError:
            return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
