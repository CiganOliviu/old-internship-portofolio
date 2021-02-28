from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import ActiveWorkingProject, FinishedProject, PlannedProject


@login_required
def projects_handler(request):

    template_name = 'views/projects.html'

    active_working_projects_query = ActiveWorkingProject.objects.all()
    finished_projects_query = FinishedProject.objects.all()
    planned_projects_query = PlannedProject.objects.filter(working_status="On Queue")

    context = {
        'active_working_projects_query': active_working_projects_query,
        'finished_projects_query': finished_projects_query,
        'planned_projects_query': planned_projects_query,
    }

    return render(request, template_name, context)


class ActiveWorkingProjectDetail(LoginRequiredMixin, generic.DetailView):

    model = ActiveWorkingProject

    template_name = 'views/projects_detail/active_working_project_detail.html'

    slug_field = 'active_working_project_slug'
    slug_url_kwarg = 'active_working_project_slug'


class PlannedProjectDetail(LoginRequiredMixin, generic.DetailView):

    model = PlannedProject

    template_name = 'views/projects_detail/planned_project_detail.html'

    slug_field = 'planned_project_slug'
    slug_url_kwarg = 'planned_project_slug'


class FinishedProjectDetail(LoginRequiredMixin, generic.DetailView):

    model = FinishedProject

    template_name = 'views/projects_detail/finished_project_detail.html'

    slug_field = 'finished_project_slug'
    slug_url_kwarg = 'finished_project_slug'
