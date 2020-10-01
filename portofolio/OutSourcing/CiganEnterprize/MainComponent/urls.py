from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('studios/', views.studio_lister, name='studio_lister'),

    path('jobs/', views.jobs_lister, name='jobs_lister'),
    path('jobs/results/', views.search_jobs_view, name='jobs_search'),
    path('jobs/appliance/', views.JobAppliance.as_view(), name='job_appliance'),

    path('internships/', views.internships_lister, name='internships_lister'),
    path('internships/results/', views.search_internships_views, name='internships_search'),
    path('internships/appliance', views.InternshipAppliance.as_view(), name='internship_appliance'),

    path('studios/<slug:studio_slug>/', views.StudioDetail.as_view(), name='studio_detail'),
    path('jobs/<slug:job_slug>/', views.JobDetail.as_view(), name='job_detail'),
    path('internships/<slug:internship_slug>/', views.InternshipDetails.as_view(), name='internship_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
