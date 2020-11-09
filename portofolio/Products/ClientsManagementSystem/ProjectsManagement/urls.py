from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_handler, name='projects_handler'),
]
