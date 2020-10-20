from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ActiveWorkingProject, FinishedProject

@login_required
def projects_handler(request):

    template_name = 'views/projects.html'

    active_projects_query = ActiveWorkingProject.objects.all()
    finished_projects_query = FinishedProject.objects.all()

    context = {
        'active_projects_query' : active_projects_query,
        'finished_projects_query' : finished_projects_query,
    }

    return render(request, template_name, context)
