from django.contrib import admin

from lab_management.models import Test, Sample, SampleType, TestRequest

register_models = [Test, Sample, SampleType, TestRequest]

admin.site.register(register_models)

