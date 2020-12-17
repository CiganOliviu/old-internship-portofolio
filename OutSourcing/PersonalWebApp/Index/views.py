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

from .setup_client_profile import create_user_in_client_detail


def clients_management_system_index(request):

    template_name = 'views/clients_management_system_index.html'

    if request.user.is_authenticated:

        create_user_in_client_detail(request.user)

        set_number_of_finished_projects_for_user(request.user)
        set_number_of_active_projects_for_user(request.user)
        set_number_of_planned_projects_for_user(request.user)
        set_number_of_requested_projects_for_user(request.user)

        save_project_from_active_projects_in_finished_projects(request.user)
        save_project_from_requested_projects_in_planned_projects(request.user)
        save_project_from_planned_projects_in_active_projects(request.user)

    return render(request, template_name)

