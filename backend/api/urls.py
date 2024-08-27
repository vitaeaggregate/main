from api.index import Index
from django.urls import include, path

urlpatterns = [
    path("", Index.as_view()),
]
