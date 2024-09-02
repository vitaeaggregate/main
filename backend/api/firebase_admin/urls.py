from django.urls import path
from api.firebase_admin.views import FireBaseSessionApiView

urlpatterns = [
    path("firebase/accounts/", FireBaseSessionApiView.as_view())
]
