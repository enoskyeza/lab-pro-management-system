from pyexpat import model
from django import forms
from . import models

class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        exclude = ('created_at', 'deleted_at', 'is_deleted')
        

# class PatientCreationForm(forms.Form):
#     surname = forms.CharField(max_length=15)
#     given_name = forms.CharField(max_length=15)
#     age = forms.IntegerField()
#     gender = forms.CharField(max_length=2)
#     Nationality = forms.CharField(max_length=10)
#     patient_id = forms.CharField(max_length=15)
#     address =forms.CharField(max_length=15)

# class PatientUpdateForm(forms.Form):
#     surname = forms.CharField(max_length=15)
#     given_name = forms.CharField(max_length=15)
#     age = forms.IntegerField()
#     gender = forms.CharField(max_length=2)
#     Nationality = forms.CharField(max_length=10)
#     patient_id = forms.CharField(max_length=15)
#     address =forms.CharField(max_length=15)
    