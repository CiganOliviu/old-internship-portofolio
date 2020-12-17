from ClientsManagement.models import ProjectsRequest

from ProjectsManagement.models import (
    ActiveWorkingProject,
    FinishedProject,
    PlannedProject
)


def save_data_into_finished_project_table(project):
    save_to_database = FinishedProject(id=project.id,
                                       user=project.user,
                                       project_name=project.project_name,
                                       project_description=project.project_description,
                                       list_of_functionalities=project.list_of_functionalities,
                                       type=project.type,
                                       date=project.date,
                                       price=project.price)
    return save_to_database


def get_filtered_data_from_planned_project(project):
    return PlannedProject.objects.filter(user=project.user,
                                         project_name=project.project_name,
                                         project_description=project.project_description,
                                         list_of_functionalities=project.list_of_functionalities,
                                         type=project.type,
                                         price=project.price,
                                         deadline_for_production=project.deadline)


def get_filtered_data_from_active_working_projects(project):
    return ActiveWorkingProject.objects.filter(id=project.id,
                                               user=project.user,
                                               project_name=project.project_name,
                                               project_description=project.project_description,
                                               list_of_functionalities=project.list_of_functionalities,
                                               type=project.type,
                                               date=project.date,
                                               price=project.price,
                                               percent_done=project.percent_done,
                                               deadline=project.deadline,
                                               ready_for_delivery=project.ready_for_delivery)


def get_filtered_data_from_projects_request(project):
    return ProjectsRequest.objects.filter(user=project.user,
                                          project_name=project.project_name,
                                          project_description=project.project_description,
                                          list_of_functionalities=project.list_of_functionalities,
                                          type=project.type)


def is_data_in_finished_projects(project):
    return FinishedProject.objects.filter(project_name=project.project_name,
                                          project_description=project.project_description,
                                          list_of_functionalities=project.list_of_functionalities,
                                          type=project.type,
                                          date=project.date,
                                          price=project.price).exists()


def save_project_from_active_projects_in_finished_projects(user):
    projects_query = ActiveWorkingProject.objects.filter(user=user)

    for project in projects_query:
        if project.ready_for_delivery:
            if not is_data_in_finished_projects(project):

                save_to_database = save_data_into_finished_project_table(project)

                save_to_database.save()

                query_planned_projects = get_filtered_data_from_planned_project(project)

                query_planned_projects.delete()

                query_active_working = get_filtered_data_from_active_working_projects(project)

                query_active_working.delete()

                query_requested_projects = get_filtered_data_from_projects_request(project)

                query_requested_projects.delete()


def save_data_into_planned_project(project):
    return PlannedProject(id=project.id,
                          user=project.user,
                          project_name=project.project_name,
                          project_description=project.project_description,
                          list_of_functionalities=project.list_of_functionalities,
                          type=project.type,
                          date=project.date,
                          price=0)


def is_data_in_planned_project(project):
    return PlannedProject.objects.filter(project_name=project.project_name,
                                         project_description=project.project_description,
                                         list_of_functionalities=project.list_of_functionalities,
                                         type=project.type,
                                         date=project.date).exists()


def save_project_from_requested_projects_in_planned_projects(user):
    projects_query = ProjectsRequest.objects.filter(user=user)

    for project in projects_query:
        if project.project_status == 'Accepted':
            if not is_data_in_planned_project(project):

                save_to_database = save_data_into_planned_project(project)

                save_to_database.save()


def save_data_into_active_working_project(project):
    return ActiveWorkingProject(id=project.id,
                                user=project.user,
                                project_name=project.project_name,
                                project_description=project.project_description,
                                list_of_functionalities=project.list_of_functionalities,
                                type=project.type,
                                price=project.price,
                                deadline=project.deadline_for_production,
                                date=project.date)


def is_data_in_active_working_project(project):
    return ActiveWorkingProject.objects.filter(project_name=project.project_name,
                                               project_description=project.project_description,
                                               list_of_functionalities=project.list_of_functionalities,
                                               type=project.type,
                                               price=project.price,
                                               deadline=project.deadline_for_production,
                                               date=project.date).exists()


def save_project_from_planned_projects_in_active_projects(user):
    projects_query = PlannedProject.objects.filter(user=user)

    for project in projects_query:
        if project.working_status == 'Current Working at':
            if not is_data_in_active_working_project(project):

                save_to_database = save_data_into_active_working_project(project)

                save_to_database.save()