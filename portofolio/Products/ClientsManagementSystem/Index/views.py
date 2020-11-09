from django.shortcuts import render

from .projects_administration import (
    save_project_from_active_projects_in_finished_projects,
    save_project_from_requested_projects_in_planned_projects,
    save_project_from_planned_projects_in_active_projects
)

from .client_projects_relationship import (
    set_number_of_finished_projects_for_user,
    set_number_of_active_projects_for_user,
    set_number_of_planned_projects_for_user,
    set_number_of_requested_projects_for_user,
)


def index(request):

    template_name = 'views/index.html'

    set_number_of_finished_projects_for_user(request.user)
    set_number_of_active_projects_for_user(request.user)
    set_number_of_planned_projects_for_user(request.user)
    set_number_of_requested_projects_for_user(request.user)

    save_project_from_active_projects_in_finished_projects(request.user)
    save_project_from_requested_projects_in_planned_projects(request.user)
    save_project_from_planned_projects_in_active_projects(request.user)

    return render(request, template_name)

