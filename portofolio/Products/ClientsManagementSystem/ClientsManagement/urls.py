from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.index, name='index'),
    path('active-working-projects/', views.active_working_projects, name='active_working_projects'),
    path('planned-projects/', views.planned_projects, name='planned_projects'),
    path('finished-projects/', views.finished_projects, name='finished_projects'),
    path('requested-projects/', views.requested_projects, name='requested_projects'),

    path('feedback/', views.ClientsFeedBackPage.as_view(), name='feedback_page'),
    path('project-request/', views.ProjectsRequestPage.as_view(), name='projects_request'),

    path('messages/', views.client_messages, name='client_messages'),
    path('messages/all', views.all_messages, name='all_messages'),
    path('messages/projects', views.projects_messages, name='projects_messages'),
    path('messages/workflow', views.workflow_messages, name='workflow_messages'),
    path('messages/others', views.other_messages, name='other_messages'),

    path('messages/<slug:message_slug>/', views.MessageDetail.as_view(), name='message_detail'),

]
