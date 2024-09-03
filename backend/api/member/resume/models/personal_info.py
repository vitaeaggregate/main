from .header import Header
from django.db import models


class PersonalInfo(models.Model):
    header = models.OneToOneField(
        Header, related_name="personal_info", on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=False)
    job_title = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    driving_license = models.CharField(max_length=50, blank=True)
    gender_pronoun = models.CharField(max_length=20, blank=True)
    marital_status = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
