from django.db import models
from core.models import BaseModel

# Create your models here.
class Patient(BaseModel):
    surname = models.CharField(max_length=15)
    given_name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=2)
    Nationality = models.CharField(max_length=10)
    patient_id = models.CharField(max_length=15)
    address =models.CharField(max_length=15)


