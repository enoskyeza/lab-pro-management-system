from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from core.models import BaseModel


class Patient(BaseModel):
    class PatientGender(models.TextChoices):
        MALE = 'M', _('MALE')
        FEMALE = 'F', _('FEMALE')

    surname = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    age = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=1, choices=PatientGender.choices)
    nationality = CountryField()
    id_number = models.CharField(verbose_name='ID Number', max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.surname} {self.given_name}'
