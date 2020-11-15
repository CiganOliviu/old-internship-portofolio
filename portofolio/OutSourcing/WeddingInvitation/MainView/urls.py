from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('invitation/', views.InvitationView.as_view(), name='invitation'),
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
