from django.urls import path
from .views import DjangoSessionApiView

urlpatterns = [
    path("sessions/", DjangoSessionApiView.as_view())
]