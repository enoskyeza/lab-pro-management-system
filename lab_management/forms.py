from django.forms import ModelForm
from django import forms

from lab_management.models import Test, TestRequest, Sample


class TestForm(ModelForm):
    class Meta:
        model = Test
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at', 'request')
        widgets = {
            'sample_id': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_collection': forms.DateTimeInput(attrs={
                'required': True,
                'type': 'datetime-local',
                'class':'form-control'}),
            'collection_site': forms.TextInput(attrs={'class':'form-select'}),
            'lab_reference': forms.TextInput(attrs={'class':'form-control'}),
        }


class TestRequestForm(ModelForm):
    class Meta:
        model = TestRequest
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')
        widgets = {
            'patient': forms.Select(attrs={'class':'form-select'}),
            'test': forms.Select(attrs={'class':'form-select'}),
            'type': forms.Select(attrs={'class':'form-select'}),
            'processing_status': forms.Select(attrs={'class':'form-select'}),
        }

