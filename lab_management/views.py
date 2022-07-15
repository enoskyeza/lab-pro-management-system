from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from lab_management.models import Sample, Test, TestRequest
from lab_management.forms import TestForm, SampleForm, TestRequestForm


def index(request):
    return render(request, 'lab_management/index.html')


class TestCreateView(CreateView):
    model = Test
    template_name = 'lab_management/create_test.html'
    form_class = TestForm
    success_url = reverse_lazy('lab_management:tests-list')


class TestUpdateView(UpdateView):
    model = Test
    template_name = 'lab_management/update_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse_lazy('lab_management:test-details', kwargs={'pk': self.object.id})


class TestListView(ListView):
    model = Test
    queryset = Test.objects.filter(is_deleted=False).all()
    template_name = 'lab_management/test_list.html'
    context_object_name = 'tests_list'
    paginate_by: 1


class TestDetailView(DetailView):
    model = Test
    template_name = 'lab_management/test_details.html'


class TestRequestCreateView(CreateView):
    model = TestRequest
    template_name = 'lab_management/create_request.html'
    form_class = TestRequestForm
    success_url = reverse_lazy('lab_management:requests-list')


class TestRequestUpdateView(UpdateView):
    model = TestRequest
    template_name = 'lab_management/update_request.html'
    form_class = TestRequestForm

    def get_success_url(self):
        return reverse_lazy('lab_management:request-details', kwargs={'pk': self.object.id})


class TestRequestListView(ListView):
    model = TestRequest
    queryset = TestRequest.objects.all()
    template_name = 'lab_management/requests_list.html'


class TestRequestDetailView(DetailView):
    model = TestRequest
    template_name = 'lab_management/request_details.html'


class SampleCreateView(CreateView):
    model = Sample
    template_name = 'lab_management/create_sample.html'
    form_class = SampleForm
