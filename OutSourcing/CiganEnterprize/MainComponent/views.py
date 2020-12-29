from django.shortcuts import render
from django.views import generic

from . import events_management
from . import update_date

from .models import Studio, Employer, Project

from Careers.models import (
    AvailableJob,
    AvailableInternship,
)


def index(request):

    template_name = 'views/index.html'

    events_management.fetch_host_event_database()
    events_management.fetch_sponsor_event_database()

    return render(request, template_name)


def studio_lister(request):

    template_name = 'views/studios/studios_lister.html'

    update_date.update_date_in_studios()

    studios_result = Studio.objects.all()
    jobs_result = AvailableJob.objects.all()[:5]
    internships_result = AvailableInternship.objects.all()[:3]

    context = {

        'studios_result': studios_result,
        'jobs_result': jobs_result,
        'internship_result': internships_result,
    }

    return render(request, template_name, context)


class StudioDetail(generic.DetailView):

    model = Studio

    template_name = 'views/studios/studio_detail.html'

    slug_field = 'studio_slug'
    slug_url_kwarg = 'studio_slug'


def employees(request):

    template_name = 'views/employees/employees.html'

    employers_results = Employer.objects.all()

    context = {
        'employers_results': employers_results,
    }

    return render(request, template_name, context)


def projects(request):

    template_name = 'views/projects/projects.html'

    projects_results = Project.objects.all()

    context = {
        'projects_results' : projects_results,
    }

    return render(request, template_name, context)