from .member.urls import urlpatterns as member_urls
from .firebase_admin.urls import urlpatterns as firebase_urls
from django.urls import include, path

routes = [
    path("", include(member_urls)),
    path("", include(firebase_urls)),
]
