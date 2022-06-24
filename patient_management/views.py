from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.views.generic.edit import CreateView
from django.views import generic

from patient_management.models import Patient
from .forms import PatientForm


# Create your views here.
def index(request):
    return render(request, 'patient_management/index.html')

class PatientCreateView(generic.edit.CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_management/create_patient.html'

    def get_success_url(self):
        return reverse('patient-details', kwargs={'pk': self.object.id})

class PatientUpdateView(generic.edit.UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_management/update_patient.html'

class PatientListView(generic.ListView):
    model = Patient
    template_name = 'patient_management/patient_list.html'
    context_object_name = 'patient_list'
    
    def get_queryset(self):
        return Patient.objects.filter(is_deleted=False).all()

class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = 'patient_management/patient_details.html'
    