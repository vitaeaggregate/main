from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.header import HeaderViewSet

router = DefaultRouter()
router.register(r"headers", HeaderViewSet)

urls = [
    path("resumes/", include(router.urls))
]
