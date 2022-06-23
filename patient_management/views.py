from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from patient_management.models import Patient
from .forms import PatientCreationForm , PatientUpdateForm


# Create your views here.
def index(request):
    return render(request, 'patient_management/index.html')

def create_patient(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/patient_management/index.html')
    else:
        form = PatientUpdateForm()

    return render(request, 'patient_management/create_patient.html', {'form': PatientUpdateForm})

def update_patient(request):

    if request.method == 'POST':
        form = PatientUpdateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('patient_management/index.html')
    else:
        form = PatientUpdateForm()

    return render(request, 'patient_management/update_patient.html', {'form': PatientUpdateForm})



class PatientListView(generic.ListView):
    model = Patient
    template_name = 'patient_management/patient_list.html'
    context_object_name = 'patient_list'
    
    def get_queryset(self):
        return Patient.objects.all()

class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = 'patient_management/patient_detail.html'
