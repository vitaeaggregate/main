
from django.http import JsonResponse
from rest_framework.views import APIView
from api.member.serializers.account import AccountSerializer

class FireBaseSessionApiView(APIView):
    def post(self, request):
        return JsonResponse(request.account)