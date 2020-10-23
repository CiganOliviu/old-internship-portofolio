from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events, name = 'events'),

    path('host-events/<slug:event_slug>/', views.HostEventDetail.as_view(), name='host_event_detail'),
    path('sponsor_events/<slug:event_slug>/', views.SponsorEventDetail.as_view(), name='sponsor_event_detail'),
    path('past-events/<slug:past_event_slug>/', views.PastEventDetail.as_view(), name='past_event_detail'),
]
