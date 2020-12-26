from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from ClientsManagement.models import (
    ClientsDetail,
    ClientsFeedBack,
    ProjectsRequest,
    MessagesToClient,
)

from ProjectsManagement.models import (
    ActiveWorkingProject,
    FinishedProject,
    PlannedProject,
)

from .forms import (
    ClientsFeedBackForm,
    ProjectsRequestForm,
    ClientsDetailForm,
)

from Index.setup_client_profile import create_user_in_client_detail

from Index.projects_administration import (
    save_project_from_active_projects_in_finished_projects,
    save_project_from_requested_projects_in_planned_projects,
    save_project_from_planned_projects_in_active_projects
)

from Index.client_projects_relationship import (
    set_number_of_finished_projects_for_user,
    set_number_of_active_projects_for_user,
    set_number_of_planned_projects_for_user,
    set_number_of_requested_projects_for_user,
)


def set_args_for_index(active_working_projects_query, client_details_query, finished_projects_query,
                       planned_projects_query, projects_request_query):
    args = {
        'client_details_query': client_details_query,
        'active_working_projects_query': active_working_projects_query,
        'finished_projects_query': finished_projects_query,
        'planned_projects_query': planned_projects_query,
        'projects_request_query': projects_request_query,
    }

    return args


@login_required
def index(request):
    template_name = 'views/client_index_view.html'

    client_details_query = ClientsDetail.objects.filter(user=request.user)[:3]
    active_working_projects_query = ActiveWorkingProject.objects.filter(user=request.user)[:3]
    finished_projects_query = FinishedProject.objects.filter(user=request.user)[:3]
    planned_projects_query = PlannedProject.objects.filter(user=request.user)[:3]
    projects_request_query = ProjectsRequest.objects.filter(user=request.user)[:3]

    args = set_args_for_index(active_working_projects_query, client_details_query, finished_projects_query,
                              planned_projects_query, projects_request_query)

    create_user_in_client_detail(request.user)

    set_number_of_finished_projects_for_user(request.user)
    set_number_of_active_projects_for_user(request.user)
    set_number_of_planned_projects_for_user(request.user)
    set_number_of_requested_projects_for_user(request.user)

    save_project_from_active_projects_in_finished_projects(request.user)
    save_project_from_requested_projects_in_planned_projects(request.user)
    save_project_from_planned_projects_in_active_projects(request.user)

    return render(request, template_name, args)


def set_args_for_active_working_projects(active_working_projects_query, client_details_query):
    args = {
        'client_details_query': client_details_query,
        'active_working_projects_query': active_working_projects_query,
    }
    return args


@login_required
def active_working_projects(request):
    template_name = 'views/projects/active_working_projects.html'

    client_details_query = ClientsDetail.objects.filter(user=request.user)
    active_working_projects_query = ActiveWorkingProject.objects.filter(user=request.user)

    args = set_args_for_active_working_projects(active_working_projects_query, client_details_query)

    return render(request, template_name, args)


def set_args_for_planned_projects(client_details_query, planned_projects_query):
    args = {
        'client_details_query': client_details_query,
        'planned_projects_query': planned_projects_query,
    }
    return args


@login_required
def planned_projects(request):
    template_name = 'views/projects/planned_projects.html'

    client_details_query = ClientsDetail.objects.filter(user=request.user)
    planned_projects_query = PlannedProject.objects.filter(user=request.user)

    args = set_args_for_planned_projects(client_details_query, planned_projects_query)

    return render(request, template_name, args)


def set_args_for_finished_projects(client_details_query, finished_projects_query):
    args = {
        'client_details_query': client_details_query,
        'finished_projects_query': finished_projects_query,
    }
    return args


@login_required
def finished_projects(request):
    template_name = 'views/projects/finished_projects.html'

    client_details_query = ClientsDetail.objects.filter(user=request.user)
    finished_projects_query = FinishedProject.objects.filter(user=request.user)

    args = set_args_for_finished_projects(client_details_query, finished_projects_query)

    return render(request, template_name, args)


def set_args_for_requested_projects(client_details_query, requested_projects_query):
    args = {
        'client_details_query': client_details_query,
        'requested_projects_query': requested_projects_query,
    }
    return args


@login_required
def requested_projects(request):
    template_name = 'views/projects/requested_projects.html'

    client_details_query = ClientsDetail.objects.filter(user=request.user)
    requested_projects_query = ProjectsRequest.objects.filter(user=request.user)

    args = set_args_for_requested_projects(client_details_query, requested_projects_query)

    return render(request, template_name, args)


class UpdateProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = 'views/update_profile/update_profile_form.html'
    final_template_name = 'views/update_profile/update_profile_form_done.html'

    def _set_default_values_for_user_detail_form(self, form, get_query_for_default):
        form.fields['first_name'].initial = get_query_for_default.first_name
        form.fields['last_name'].initial = get_query_for_default.last_name
        form.fields['client_description'].initial = get_query_for_default.client_description
        form.fields['email'].initial = get_query_for_default.email
        form.fields['phone_number'].initial = get_query_for_default.phone_number
        form.fields['website'].initial = get_query_for_default.website
        form.fields['social_media_presence'].initial = get_query_for_default.social_media_presence
        form.fields['profile_image'].initial = get_query_for_default.profile_image
        form.fields['type_of_client'].initial = get_query_for_default.type_of_client

    def get(self, request):

        form = ClientsDetailForm()

        get_query_for_default = ClientsDetail.objects.get(user=request.user)

        self._set_default_values_for_user_detail_form(form, get_query_for_default)

        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _replace_user_details(self, database_object):

        if ClientsDetail.objects.filter(user=database_object.user).exists():
            process_query = ClientsDetail.objects.get(user=database_object.user)

            process_query.profile_image = database_object.profile_image
            process_query.first_name = database_object.first_name
            process_query.last_name = database_object.last_name
            process_query.client_description = database_object.client_description
            process_query.email = database_object.email
            process_query.phone_number = database_object.phone_number
            process_query.website = database_object.website
            process_query.social_media_presence = database_object.social_media_presence

            process_query.save()

    def post(self, request):

        form = ClientsDetailForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            self._replace_user_details(post)

        return render(request, self.final_template_name)


class ClientsFeedBackPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'views/clients_feedback/feedback.html'
    final_template_name = 'views/clients_feedback/feedback_final.html'

    def get(self, request):

        form = ClientsFeedBackForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user=database_object.user, title=database_object.title,
                                        content=database_object.content).exists():
            return False

        return True

    def post(self, request):

        form = ClientsFeedBackForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            if self._validate_save(ClientsFeedBack, post):
                post.save()

        return render(request, self.final_template_name)


class ProjectsRequestPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'views/projects_requests/project_request_perform.html'
    final_template_name = 'views/projects_requests/project_request_perform_done.html'

    def get(self, request):

        form = ProjectsRequestForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user=database_object.user, project_name=database_object.project_name,
                                        project_description=database_object.project_description,
                                        list_of_functionalities=database_object.list_of_functionalities,
                                        type=database_object.type).exists():
            return False

        return True

    def post(self, request):

        form = ProjectsRequestForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            if self._validate_save(ProjectsRequest, post):
                post.save()

        return render(request, self.final_template_name)


@login_required()
def client_messages(request):
    template_name = 'views/client_messages/messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user)

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


@login_required()
def all_messages(request):
    template_name = 'views/client_messages/all_messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user)[:5]

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


@login_required()
def projects_messages(request):
    template_name = 'views/client_messages/projects_messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user, type_of_message='Projects Reference')

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


@login_required()
def workflow_messages(request):
    template_name = 'views/client_messages/workflow_messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user, type_of_message='Workflow Reference')

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


@login_required()
def other_messages(request):
    template_name = 'views/client_messages/other_messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user, type_of_message='Others')

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


class MessageDetail(LoginRequiredMixin, generic.DetailView):
    model = MessagesToClient

    template_name = 'views/client_messages/message_detail.html'

    slug_field = 'message_slug'
    slug_url_kwarg = 'message_slug'


class RequestedProjectDetail(LoginRequiredMixin, generic.DetailView):
    model = ProjectsRequest

    template_name = 'views/projects_detail/requested_project_detail.html'

    slug_field = 'project_request_slug'
    slug_url_kwarg = 'project_request_slug'
