from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.PatientListView.as_view(), name='patient-list'),
    # path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-details'),
    path('new/', views.create_patient, name='create-patient'),
    path('update/', views.update_patient, name='update-patient'),
]
