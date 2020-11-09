from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
