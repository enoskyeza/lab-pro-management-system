from django.contrib import admin
from lab_management.models import Test, Sample, SampleType, TestRequest

# Register your models here.

my_models = [Test, Sample, SampleType, TestRequest]
admin.site.register(my_models)

