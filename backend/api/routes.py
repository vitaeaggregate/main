from django.urls import include, path
from .member.urls import router as member_router

routes = [
    path("", include(member_router.urls)),
]
