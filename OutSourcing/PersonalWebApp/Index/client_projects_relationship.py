from ClientsManagement.models import (
    ClientsDetail,
    ProjectsRequest
)

from ProjectsManagement.models import (
    ActiveWorkingProject,
    FinishedProject,
    PlannedProject
)


def get_number_of_finished_projects_for_user(user):
    result = FinishedProject.objects.filter(user=user)

    return result.count()


def get_number_of_active_projects_for_user(user):
    result = ActiveWorkingProject.objects.filter(user=user)

    return result.count()


def get_number_of_planned_projects_for_user(user):
    result = PlannedProject.objects.filter(user=user)

    return result.count()


def get_number_of_requested_projects_for_user(user):
    result = ProjectsRequest.objects.filter(user=user)

    return result.count()


def set_number_of_finished_projects_for_user(user):
    user_query = ClientsDetail.objects.get(user=user)

    user_query.number_of_finished_projects = get_number_of_finished_projects_for_user(user)

    user_query.save()


def set_number_of_active_projects_for_user(user):
    user_query = ClientsDetail.objects.get(user=user)

    user_query.number_of_projects_in_progress = get_number_of_active_projects_for_user(user)

    user_query.save()


def set_number_of_planned_projects_for_user(user):
    user_query = ClientsDetail.objects.get(user=user)

    user_query.number_of_planned_projects = get_number_of_planned_projects_for_user(user)

    user_query.save()


def set_number_of_requested_projects_for_user(user):
    user_query = ClientsDetail.objects.get(user=user)

    user_query.number_of_proposed_projects = get_number_of_requested_projects_for_user(user)

    user_query.save()
