from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q
from .forms import ApplianceForm, InternshipApplianceForm
from MainComponent import update_date
from .models import Studio
from Careers.models import (
    AvailableJob,
    AvailableInternship,
    JobsAppliance,
    InternshipsAppliance,
)


def get_data_from_available_job(query):

    results = AvailableJob.objects.filter(Q(post__icontains=query) | Q(location__city__icontains=query)
                                          | Q(description__icontains=query) | Q(requirements__icontains=query)
                                          | Q(one_day__icontains=query) | Q(job_type__icontains=query)
                                          | Q(perks__icontains=query))
    return results


def search_jobs_view(request):
    template_name = 'views/jobs/jobs_results.html'

    update_date.update_date_in_studios()

    studios_result = Studio.objects.all()

    query = request.GET.get('q')

    if query:
        results = get_data_from_available_job(query)
    else:
        redirect('/jobs')

    context = {
        'studios_result': studios_result,
        'results': results,
    }

    return render(request, template_name, context)


def jobs_lister(request):
    template_name = 'views/jobs/jobs_lister.html'

    update_date.update_date_in_studios()

    studios_result = Studio.objects.all()
    jobs_result = AvailableJob.objects.all()

    context = {
        'studios_result': studios_result,
        'jobs_result': jobs_result,
    }

    return render(request, template_name, context)


class JobDetail(generic.DetailView):
    model = AvailableJob

    template_name = 'views/jobs/job_detail.html'

    slug_field = 'job_slug'
    slug_url_kwarg = 'job_slug'


class JobAppliance(generic.TemplateView):
    template_name = 'views/appliance/job_appliance.html'
    final_template_name = 'views/appliance/job_appliance_send.html'

    def get(self, request):

        form = ApplianceForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(first_name=database_object.first_name, last_name=database_object.last_name,
                                            email=database_object.email,
                                            years_of_experience=database_object.years_of_experience,
                                            description_of_skills=database_object.description_of_skills,
                                            career=database_object.career).exists():
            return True

        return False

    def post(self, request):

        form = ApplianceForm(request.POST, request.FILES)

        print(form.is_valid())

        if form.is_valid():

            post = form.save(commit=False)

            if self._validate_save(JobsAppliance, post):
                form.save()

        return render(request, self.final_template_name)


def internships_lister(request):
    template_name = 'views/internships/internships_lister.html'

    update_date.update_date_in_studios()

    internships_results = AvailableInternship.objects.all()
    studios_result = Studio.objects.all()

    context = {
        'internships_results': internships_results,
        'studios_result': studios_result,
    }

    return render(request, template_name, context)


def get_data_from_available_internship(query):

    results = AvailableInternship.objects.filter(Q(post__icontains=query) | Q(location__city__icontains=query)
                                                 | Q(description__icontains=query) | Q(requirements__icontains=query)
                                                 | Q(one_day__icontains=query) | Q(job_type__icontains=query)
                                                 | Q(perks__icontains=query))
    return results


def search_internships_views(request):
    template_name = 'views/internships/internships_results.html'

    update_date.update_date_in_studios()

    studios_result = Studio.objects.all()

    query = request.GET.get('q')

    if query:
        results = get_data_from_available_internship(query)
    else:
        redirect('/internships')

    context = {
        'studios_result': studios_result,
        'results': results,
    }

    return render(request, template_name, context)


class InternshipDetails(generic.DetailView):
    model = AvailableInternship

    template_name = 'views/internships/internship_details.html'

    slug_field = 'internship_slug'
    slug_url_kwarg = 'internship_slug'


class InternshipAppliance(generic.TemplateView):
    template_name = 'views/appliance/internship_appliance.html'
    final_template_name = 'views/appliance/internship_appliance_send.html'

    def get(self, request):

        form = InternshipApplianceForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(first_name=database_object.first_name, last_name=database_object.last_name,
                                            email=database_object.email,
                                            description_of_skills=database_object.description_of_skills,
                                            career=database_object.career).exists():
            return True

        return False

    def post(self, request):

        form = InternshipApplianceForm(request.POST, request.FILES)

        print(form.is_valid())

        if form.is_valid():

            post = form.save(commit=False)

            if self._validate_save(InternshipsAppliance, post):
                form.save()

        return render(request, self.final_template_name)
