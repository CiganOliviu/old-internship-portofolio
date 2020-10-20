from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from ClientsManagement.models import (
    FeedBack,
    AskProject,
    DirectClientContact,
)

from .forms import (
    FeedBackForm,
    AskProjectForm,
    DirectClientContactForm,
)

@login_required
def index(request):

    template_name = 'views/client_index_view.html'

    return render(request, template_name)

class FeedBackPage(LoginRequiredMixin, generic.TemplateView):

    template_name = 'views/feedback_pages/feedback.html'
    final_template_name = 'views/feedback_pages/feedback_final.html'

    def get(self, request):

        form = FeedBackForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user = database_object.user, title = database_object.title,
                                            content = database_object.content).exists():
            return False

        return True

    def post(self, request):

        form = FeedBackForm(request.POST)

        if form.is_valid():

            post = form.save(commit = False)
            post.user = request.user

            if self._validate_save(FeedBack, post):
                post.save()

        return render(request, self.final_template_name)

class AskProjectPage(LoginRequiredMixin, generic.TemplateView):

    template_name = 'views/ask_project_pages/ask_project.html'
    final_template_name = 'views/ask_project_pages/ask_project_final.html'

    def get(self, request):

        form = AskProjectForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user = database_object.user, project_name = database_object.project_name,
                                            project_description = database_object.project_description,
                                            list_of_functionalities = database_object.list_of_functionalities,
                                            type = database_object.type).exists():

                                            return False

        return True

    def post(self, request):

        form = AskProjectForm(request.POST)

        if form.is_valid():

            post = form.save(commit = False)
            post.user = request.user

            if self._validate_save(AskProject, post):
                post.save()

        return render(request, self.final_template_name)

class ClientContactPage(LoginRequiredMixin, generic.TemplateView):

    template_name = 'views/direct_client_contact/direct_client_contact.html'
    final_template_name = 'views/direct_client_contact/direct_client_contact_final.html'

    def get(self, request):

        form = DirectClientContactForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user = database_object.user,
                                        title = database_object.title,
                                        message = database_object.message).exists():

                                        return False

        return True


    def post(self, request):

        form = DirectClientContactForm(request.POST)

        if form.is_valid():

            post = form.save(commit = False)
            post.user = request.user

            if self._validate_save(DirectClientContact, post):
                post.save()

        return render(request, self.final_template_name)
