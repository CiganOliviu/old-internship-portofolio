from django.urls import path

from . import views

urlpatterns = [
    path('host-events/', views.host_events, name = 'host_events'),
    path('sponsor-events/', views.sponsor_events, name = 'sponsor_events'),
    path('past-events/', views.past_events, name = 'past_events'),

    path('host-events/<slug:event_slug>/', views.HostEventDetail.as_view(), name = 'host_event_detail'),
    path('sponsor_events/<slug:event_slug>/', views.SponsorEventDetail.as_view(), name = 'sponsor_event_detail'),
    path('past-events/<slug:past_event_slug>/', views.PastEventDetail.as_view(), name = 'past_event_detail'),
]
