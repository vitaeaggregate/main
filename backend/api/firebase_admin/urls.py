from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.firebase_admin.views import FireBaseSessionViewSet

router = DefaultRouter()

router.register(r"firebase/accounts", FireBaseSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]