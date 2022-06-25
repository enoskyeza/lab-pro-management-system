from django.shortcuts import render
from django.urls import reverse
from lab_management.models import Test
from lab_management.forms import TestForm
from django.views.generic import *

# Create your views here.
def index(request):
    return render(request, 'lab_management/index.html')

class TestCreateView(CreateView):
    model = Test
    template_name = 'lab_management/create_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse('test-list', kwargs={'pk': self.object.id})

class TestUpdateView(UpdateView):
    model = Test
    template_name = 'lab_management/update_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse('test-list', kwargs={'pk': self.object.id})


class TestListView(ListView):
    model = Test
    template_name = 'lab_management/test_list.html'
    context_object_name = 'tests_list'

    def get_queryset(self):
        return Test.objects.filter(is_deleted=False).all()    

class TestDetailView(DetailView):
    model = Test
    template_name = 'lab_management/test_details.html'


