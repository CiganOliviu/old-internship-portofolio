from django.urls import path
from . import views

urlpatterns = [
    path('HomeManagement', views.index, name = 'index'),
]
