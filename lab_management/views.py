from django.shortcuts import render
from django.urls import reverse
from lab_management.models import Sample, Test, TestRequest
from lab_management.forms import TestForm, SampleForm, TestRequestForm
from django.views.generic import *

# Create your views here.
def index(request):
    return render(request, 'lab_management/index.html')

class TestCreateView(CreateView):
    model = Test
    template_name = 'lab_management/create_test.html'
    form_class = TestForm
    def get_success_url(self):
        return reverse('tests-list')

class TestUpdateView(UpdateView):
    model = Test
    template_name = 'lab_management/update_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse('tests-list')


class TestListView(ListView):
    model = Test
    template_name = 'lab_management/test_list.html'
    context_object_name = 'tests_list'

    def get_queryset(self):
        return Test.objects.filter(is_deleted=False).all()    

class TestDetailView(DetailView):
    model = Test
    template_name = 'lab_management/test_details.html'

class TestRequestCreateView(CreateView):
    model = TestRequest
    template_name = 'lab_management/create_request.html'
    form_class = TestRequestForm

    def get_success_url(self):
     return reverse('requests-list')

class TestRequestUpdateView(UpdateView):
    model = TestRequest
    template_name = 'lab_management/update_request.html'
    form_class = TestRequestForm

    def get_success_url(self):
        return reverse('request-details', kwargs={'pk': self.object.id})

class TestRequestListView(ListView):
    model: TestRequest
    template_name = 'lab_management/requests_list.html'
    context_object_name = 'requests_list'
    
    def get_queryset(self):
        return TestRequest.objects.all()

class TestRequestDetailView(DetailView):
    model = TestRequest
    template_name = 'lab_management/request_details.html'

class SampleCreateView(CreateView):
    model = Sample
    template_name = 'lab_management/create_sample.html'
    form_class = SampleForm




