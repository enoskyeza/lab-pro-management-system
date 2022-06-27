from django.urls import path

from patient_management import views
from patient_management.views import PatientCreateView, PatientDetailView, PatientListView, PatientUpdateView


app_name = 'patient_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('list', PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-details'),
    path('new/', PatientCreateView.as_view(), name='create-patient'),
    path('update/<int:pk>/', PatientUpdateView.as_view(), name='update-patient'),
]
