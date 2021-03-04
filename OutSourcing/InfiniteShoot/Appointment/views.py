from django.shortcuts import render
from django.views import generic
from Appointment.models import Appointment
from Appointment.form import AppointmentForm


class AppointmentView(generic.TemplateView):
    template_name = 'appointment/appointment_view.html'
    final_template_name = 'appointment/post_appointment.html'

    def get(self, request):
        form = AppointmentForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name,  args)

    def post(self, request):

        form = AppointmentForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            if self._validate_save(Appointment, post):
                form.save()

        return render(request, self.final_template_name)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(email=database_object.email).exists():
            return True

        return False
