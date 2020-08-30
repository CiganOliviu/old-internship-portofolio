from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from MainView.forms import InvitationForm
from MainView.models import ConfirmAnswer, GuestEnvironmentDetail

class InvitationView(LoginRequiredMixin, TemplateView):

    template_name = 'home/invitation_form.html'
    final_template_name = 'home/invitation.html'

    def _add_user_if_missing(self, database_name, database_object):

        if not database_name.objects.filter(user = database_object.user).exists():
            process_query = database_name(user = database_object.user)
            process_query.save()

    def _did_the_user_respond(self, database_object):

        if ConfirmAnswer.objects.filter(user = database_object.user, answer_sent = True).exists():
            return True

    def _return_guest_database_object(self, database_object):

        result = GuestEnvironmentDetail.objects.filter(user = database_object.user)

        return result

    def get(self, request):

        form = InvitationForm()

        post = form.save(commit=False)
        post.user = request.user

        self._add_user_if_missing(ConfirmAnswer, post)

        if self._did_the_user_respond(post):

            self._add_user_if_missing(GuestEnvironmentDetail, post)

            guests = self._return_guest_database_object(post)

            args = { 'guests': guests }

            return render(request, self.final_template_name, args)

        args = { 'form': form }

        return render(request, self.template_name, args)

    def _replace_user_answer(self, database_object):

        if ConfirmAnswer.objects.filter(user = database_object.user, answer_sent = False).exists():

            process_query = ConfirmAnswer.objects.get(user = database_object.user)
            process_query.answer_sent = True
            process_query.save()

    def post(self, request):

        form = InvitationForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            self._replace_user_answer (post)

            self._add_user_if_missing(GuestEnvironmentDetail, post)

            guests = self._return_guest_database_object(post)
            text = form.cleaned_data['answer_sent']

        args = { 'text': text, 'guests' : guests}

        return render(request, self.final_template_name, args)

def index(request):

    template_name = 'home/index.html'

    return render(request, template_name)
