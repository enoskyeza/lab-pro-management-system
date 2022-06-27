from django.urls import path
from . import views


app_name = 'patient_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-details'),
    path('new/', views.PatientCreateView.as_view(), name='create-patient'),
    path('update/<int:pk>/', views.PatientUpdateView.as_view(), name='update-patient'),
]
