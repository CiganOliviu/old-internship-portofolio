from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('studios/', views.studio_lister, name = 'studio_lister'),
    path('jobs/', views.jobs_lister, name = 'jobs_lister'),
    path('jobs/results/', views.search_jobs_view, name = 'jobs_search'),
    path('jobs/appliance/', views.JobAppliance.as_view(), name = 'job_appliance'),

    path('studios/<slug:studio_slug>/', views.StudioDetail.as_view(), name='studio_detail'),
    path('jobs/<slug:job_slug>/', views.JobDetail.as_view(), name='job_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
