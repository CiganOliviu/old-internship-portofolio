from django.shortcuts import render
from django.views import generic

from .models import PastEvent, SponsorEvent, HostEvent

def host_events(request):

    template_name = 'views/events/host/host_events.html'

    host_events_query = HostEvent.objects.all()

    context = {

        'host_events_query' : host_events_query,
    }

    return render(request, template_name, context)

def sponsor_events(request):

    template_name = 'views/events/sponsor/sponsor_events.html'

    sponsor_events_query = SponsorEvent.objects.all()

    context = {

        'sponsor_events_query' : sponsor_events_query,
    }

    return render(request, template_name, context)

def past_events(request):

    template_name = 'views/events/past/past_events.html'

    past_events_query = PastEvent.objects.all()

    context = {

        'past_events_query' : past_events_query,
    }

    return render(request, template_name, context)

class HostEventDetail(generic.DetailView):

    model = HostEvent

    template_name = 'views/events/host/host_event_detail.html'

    slug_field = 'event_slug'
    slug_url_kwarg = 'event_slug'

class SponsorEventDetail(generic.DetailView):

    model = SponsorEvent

    template_name = 'views/events/sponsor/sponsor_event_detail.html'

    slug_field = 'event_slug'
    slug_url_kwarg = 'event_slug'

class PastEventDetail(generic.DetailView):

    model = PastEvent

    template_name = 'views/events/past/past_event_detail.html'

    slug_field = 'past_event_slug'
    slug_url_kwarg = 'past_event_slug'
