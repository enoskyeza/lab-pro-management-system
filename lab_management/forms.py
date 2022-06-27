from django.forms import ModelForm

from lab_management.models import Test, TestRequest, Sample


class TestForm(ModelForm):
    class Meta:
        model = Test
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')


class TestRequestForm(ModelForm):
    class Meta:
        model = TestRequest
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')
