from django.contrib import admin
from lab_management.models import Test, Sample, SampleType, TestRequest

# Register your models here.

all_models = [Test, Sample, SampleType, TestRequest]
admin.site.register(all_models)

