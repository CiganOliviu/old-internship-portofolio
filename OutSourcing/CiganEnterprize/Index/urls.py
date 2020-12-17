from django.urls import path
from . import views

urlpatterns = [
    path('clients-management-system/', views.clients_management_system_index, name='clients_management_system_index'),
]