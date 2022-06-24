from django.contrib import admin
from .models import Patient 

# Register your models here.
# class PatientAdmin(admin.ModelAdmin):
#     fields = ['surname', 'given_name', 'age', 'sex', 'contact', 'gender', 'nationality', 'patient_id', 'address' ]

admin.site.register(Patient)
