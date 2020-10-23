from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('studios/', views.studio_lister, name='studio_lister'),
    path('employees/', views.employees, name='employees'),

    path('studios/<slug:studio_slug>/', views.StudioDetail.as_view(), name='studio_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
