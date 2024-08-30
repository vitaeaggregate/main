from ..models.header import Header
from django.db import models


class ProfessionalExp(models.model):
    resume = models.ForeignKey(Header, on_delete=models.CASCADE, blank=False)
    full_name = models.CharField(blank=False)
    job_title = models.CharField(blank=False)
    email = models.EmailField()
    phone_number = models.CharField()
    address = models.CharField()
    date_of_birth = models.IntegerField()
    drivers_license = models.BooleanField()
