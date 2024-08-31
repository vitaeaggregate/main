
from api.member.models.account import Account
from .serializers import FirebaseAccountSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth


class FireBaseSessionViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter().exclude(firebase_uid="")
    serializer_class = FirebaseAccountSerializer

    def create(self, request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return Response({'status': 'error', 'message': 'Authorization header missing'}, status=401)

        firebase_token = auth_header.split(" ")[1]

        if not firebase_token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verify Firebase token
            decoded_token = auth.verify_id_token(firebase_token)
            firebase_uid = decoded_token["uid"]
            email = decoded_token.get("email")

            # Check if user already exists
            account, created = Account.objects.get_or_create(
                firebase_uid=firebase_uid,
                defaults={'email': email}
            )

            # Serialize the account data
            serializer = self.get_serializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

        except auth.InvalidIdTokenError:
            return Response({'status': 'error', 'message': 'Invalid token'}, status=401)
