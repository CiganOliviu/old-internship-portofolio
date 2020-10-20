from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('feedback/', views.FeedBackPage.as_view(), name = 'feedback_page'),
    path('ask-project/', views.AskProjectPage.as_view(), name = 'ask_project'),
    path('client-contact/', views.ClientContactPage.as_view(), name = 'client_contact'),
]
