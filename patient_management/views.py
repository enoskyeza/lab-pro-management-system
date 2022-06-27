from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from patient_management.models import Patient
from .forms import PatientForm


def index(request):
    return render(request, 'patient_management/index.html')


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_management/create_patient.html'

    def get_success_url(self):
        return reverse('patient_management:patient-list', kwargs={'pk': self.object.id})


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_management/update_patient.html'
    success_url = reverse('patient_management:patient-details')


class PatientListView(ListView):
    model = Patient
    queryset = Patient.objects.all().filter(is_deleted=False)
    template_name = 'patient_management/patient_list.html'
    context_object_name = 'patient_list'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_management/patient_details.html'
