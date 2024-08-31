from django.apps import AppConfig
from . import config

class FirebaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.firebase_admin"
