from unicodedata import name
from lab_management.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='test-index-view'),
    path('list', TestListView.as_view(), name='tests-list'),
    path('<int:pk>/', TestDetailView.as_view(), name='test-details'),
    path('new/', TestCreateView.as_view(), name='create-test'),
    path('update/<int:pk>/', TestUpdateView.as_view(), name='update-test'),
    path('newrequest/', TestRequestCreateView.as_view(), name='create-request'),
    path('requests/<int:pk>/', TestRequestDetailView.as_view(), name='request-details'),
    path('requests/', TestRequestListView.as_view(), name='requests-list'),
    path('requestupdate/<int:pk>', TestRequestUpdateView.as_view(), name='update-request'),
    path('sample/', SampleCreateView.as_view(), name='create-sample'),
]

