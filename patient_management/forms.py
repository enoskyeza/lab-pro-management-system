from django import forms

from . import models


class PatientForm(forms.ModelForm):
    # def __innit__(self, *args, **kwargs):
    #     super(PatientForm, self).__init__(*args, **kwargs)
    #     self.fields["surname"].widget.attrs.update({
    #         'required':'',
    #         'name':'surname',
    #         'id':'surname',
    #         'type':'password',
    #         'class':'form-control',
    #         })

    class Meta:
        model = models.Patient
        exclude = ('created_at', 'deleted_at', 'is_deleted', 'updated_at')
        widgets = {
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'given_name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.DateInput(attrs={
                'required': True,
                'type': 'date',
                'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-select'}),
            'id_number': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }