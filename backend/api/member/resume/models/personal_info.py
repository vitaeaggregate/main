from .header import Header
from django.db import models


class PersonalInfo(models.Model):
    resume = models.OneToOneField(Header, on_delete=models.CASCADE, blank=False)
    full_name = models.CharField(blank=False)
    job_title = models.CharField(blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True)
    address = models.CharField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    driving_license = models.CharField(blank=True)
    gender_pronoun = models.CharField(blank=True)
    marital_status = models.CharField(blank=True)
    nationality = models.CharField(blank=True)
