from django.db import models
from core.models import BaseModel
from patient_management.models import Patient

# Create your models here.
class StatusChoices(models.TextChoices):
    STARTED = 'STARTED', ('STARTED')
    IN_PROGRESS = 'IN PROGRESS', ('IN PROGRESS')
    COMPLETE = 'COMPLETED', ('COMPLETED')


class Test(BaseModel):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SampleType(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sample(BaseModel):
    type = models.ForeignKey(SampleType, null=True, on_delete=models.SET_NULL)
    collection_site = models.CharField(max_length=50)
    date_of_collection = models.DateTimeField()
    lab_reference = models.CharField(max_length=150)
    date_of_result = models.DateTimeField()

class TestRequest(BaseModel):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, null=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, null=True, on_delete=models.SET_NULL)
    proccessing_status = models.CharField(max_length=50, choices=StatusChoices.choices)