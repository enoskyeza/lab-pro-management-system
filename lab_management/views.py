from django.shortcuts import render
from django.urls import reverse
from .models import Test
from .forms import TestForm
from django.views.generic import *

# Create your views here.
def index(request):
    return render(request, 'lab_management/index.html')

class TestCreateView(CreateView):
    model = Test
    template_name = 'lab_management/create_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse('test-details', kwargs={'pk': self.object.id})

class TestUpdateView(UpdateView):
    model = Test
    template_name = 'lab_management/update_test.html'
    form_class = TestForm

    def get_success_url(self):
        return reverse('test-details', kwargs={'pk': self.object.id})


class TestListView(ListView):
    model = Test
    template_name = 'lab_management/test_list.html'
    context_object_name = 'test_list'

    def get_queryset(self):
        return Test.objects.filter(is_deleted=False).all()    

class TestDetailView(DetailView):
    model = Test
    template_name = 'lab_management/test_list.html'


