
from django.http import JsonResponse
from rest_framework.views import APIView

class FireBaseSessionApiView(APIView):
    def post(self, request):
        return JsonResponse(request.account)