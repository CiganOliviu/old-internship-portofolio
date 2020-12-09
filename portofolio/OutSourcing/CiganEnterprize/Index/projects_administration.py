from ClientsManagement.models import ProjectsRequest

from ProjectsManagement.models import (
    ActiveWorkingProject,
    FinishedProject,
    PlannedProject
)


def save_project_from_active_projects_in_finished_projects(user):
    projects_query = ActiveWorkingProject.objects.filter(user=user)

    for project in projects_query:
        if project.ready_for_delivery:
            if not FinishedProject.objects.filter(project_name=project.project_name,
                                                  project_description=project.project_description,
                                                  list_of_functionalities=project.list_of_functionalities,
                                                  type=project.type,
                                                  date=project.date,
                                                  price=project.price).exists():
                save_to_database = FinishedProject(id=project.id,
                                                   user=project.user,
                                                   project_name=project.project_name,
                                                   project_description=project.project_description,
                                                   list_of_functionalities=project.list_of_functionalities,
                                                   type=project.type,
                                                   date=project.date,
                                                   price=project.price)

                save_to_database.save()
                
                query_planned_projects = PlannedProject.objects.filter(user=project.user,
                                                                       project_name=project.project_name,
                                                                       project_description=project.project_description,
                                                                       list_of_functionalities=project.list_of_functionalities,
                                                                       type=project.type,
                                                                       price=project.price,
                                                                       deadline_for_production=project.deadline)

                query_planned_projects.delete()

                query_active_working = ActiveWorkingProject.objects.filter(id=project.id,
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

                query_active_working.delete()


                query_requested_projects = ProjectsRequest.objects.filter(user=project.user,
                                                                          project_name=project.project_name,
                                                                          project_description=project.project_description,
                                                                          list_of_functionalities=project.list_of_functionalities,
                                                                          type=project.type)

                query_requested_projects.delete()


def save_project_from_requested_projects_in_planned_projects(user):
    projects_query = ProjectsRequest.objects.filter(user=user)

    for project in projects_query:
        if project.project_status == 'Accepted':
            if not PlannedProject.objects.filter(project_name=project.project_name,
                                                 project_description=project.project_description,
                                                 list_of_functionalities=project.list_of_functionalities,
                                                 type=project.type,
                                                 date=project.date).exists():
                save_to_database = PlannedProject(id=project.id,
                                                  user=project.user,
                                                  project_name=project.project_name,
                                                  project_description=project.project_description,
                                                  list_of_functionalities=project.list_of_functionalities,
                                                  type=project.type,
                                                  date=project.date,
                                                  price=0)

                save_to_database.save()


def save_project_from_planned_projects_in_active_projects(user):
    projects_query = PlannedProject.objects.filter(user=user)

    for project in projects_query:
        if project.working_status == 'Current Working at':
            if not ActiveWorkingProject.objects.filter(project_name=project.project_name,
                                                       project_description=project.project_description,
                                                       list_of_functionalities=project.list_of_functionalities,
                                                       type=project.type,
                                                       price=project.price,
                                                       deadline=project.deadline_for_production,
                                                       date=project.date).exists():
                save_to_database = ActiveWorkingProject(id=project.id,
                                                        user=project.user,
                                                        project_name=project.project_name,
                                                        project_description=project.project_description,
                                                        list_of_functionalities=project.list_of_functionalities,
                                                        type=project.type,
                                                        price=project.price,
                                                        deadline=project.deadline_for_production,
                                                        date=project.date)

                save_to_database.save()

