from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_handler, name='projects_handler'),

    path('active-working-project-detail/<slug:active_working_project_slug>/', views.ActiveWorkingProjectDetail.as_view(),	
         name='active_working_project_detail'),

    path('planned-project-detail/<slug:planned_project_slug>/', views.PlannedProjectDetail.as_view(),
         name='planned_project_detail'),

    path('finished-project-detail/<slug:finished_project_slug>/', views.FinishedProjectDetail.as_view(),
         name='finished_project_detail'),

]
