from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='test-index-view'),
    path('list', TestListView.as_view(), name='test-list'),
    path('<int:pk>/', TestDetailView.as_view(), name='test-details'),
    path('new/', TestCreateView.as_view(), name='create-test'),
    path('update/<int:pk>/', TestUpdateView.as_view(), name='update-test'),
]