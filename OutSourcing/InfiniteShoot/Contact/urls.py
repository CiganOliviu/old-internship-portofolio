from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact_view'),
    path('newsletter/', views.NewsletterView.as_view(), name='newsletter_view'),
]

