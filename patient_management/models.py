from django.db import models
from core.models import BaseModel
# from django_countries.fields import CountryField

# Create your models here.
class Patient(BaseModel):
    surname = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50, null=True)
    identification = models.CharField(max_length=50, blank=True)
    address =models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{} {}'.format(self.surname, self.given_name)


