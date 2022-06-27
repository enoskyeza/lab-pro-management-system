from django.db import models
from core.models import BaseModel
from patient_management.models import Patient

# Create your models here.

class Test(BaseModel):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    duration = models.FloatField()

    def __str__(self):
        return self.name

class SampleType(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sample(BaseModel):
    type = models.ForeignKey(SampleType, null=True, on_delete=models.SET_NULL)
    collection_site = models.CharField(max_length=50)
    date_of_collection = models.DateField()
    lab_reference = models.PositiveIntegerField(null=True, blank=True)
    date_of_result = models.DateField()

class TestRequest(BaseModel):
    class StatusChoices(models.TextChoices):
        STARTED = 'started', ('STARTED')
        IN_PROGRESS = 'in_progress', ('IN PROGRESS')
        COMPLETE = 'completed', ('COMPLETED')

    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, null=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, blank=True, null=True, on_delete=models.SET_NULL)
    proccessing_status = models.CharField(max_length=50, choices=StatusChoices.choices)