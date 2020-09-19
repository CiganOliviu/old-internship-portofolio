from django.urls import path

from . import views

urlpatterns = [
    path('newsletter/', views.NewsletterView.as_view(), name = 'newsletter'),
    path('contact/', views.FormularContact.as_view(), name = 'formular_contact'),
]
