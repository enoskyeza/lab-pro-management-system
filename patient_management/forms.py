from pyexpat import model
from django import forms
from . import models

class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        exclude = ('created_at', 'deleted_at', 'is_deleted')

    