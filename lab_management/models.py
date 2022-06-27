from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from patient_management.models import Patient


class Test(BaseModel):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    duration = models.FloatField(help_text='Enter test duration in hours i.e: 1.5 hours')

    def __str__(self):
        return self.name


class SampleType(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sample(BaseModel):
    sample_id = models.CharField(max_length=10, unique=True)
    type = models.ForeignKey(SampleType, null=True, on_delete=models.SET_NULL)
    collection_site = models.CharField(max_length=50)
    date_of_collection = models.DateTimeField(default=timezone.now)
    lab_reference = models.PositiveIntegerField(null=True, blank=True)
    date_of_result = models.DateTimeField(null=True, blank=True)


class TestRequest(BaseModel):
    class TestRequestProgressStatus(models.TextChoices):
        STARTED = 'started', _('STARTED')
        IN_PROGRESS = 'in_progress', _('IN PROGRESS')
        COMPLETE = 'completed', _('COMPLETED')

    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, null=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, blank=True, null=True, on_delete=models.SET_NULL)
    processing_status = models.CharField(max_length=50, choices=TestRequestProgressStatus.choices)
