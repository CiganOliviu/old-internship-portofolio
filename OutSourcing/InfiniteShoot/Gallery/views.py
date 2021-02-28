from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from .models import ImagesClient, PlatformPresentationImage
from Gallery.form import ImageClientForm


def gallery_view(request):
    template_name = "gallery/gallery_view.html"

    images_for_first_column = PlatformPresentationImage.objects.filter(column="First Column")
    images_for_second_column = PlatformPresentationImage.objects.filter(column="Second Column")
    images_for_third_column = PlatformPresentationImage.objects.filter(column="Third Column")
    images_for_fourth_column = PlatformPresentationImage.objects.filter(column="Fourth Column")

    context = {
        'images_for_first_column': images_for_first_column,
        'images_for_second_column': images_for_second_column,
        'images_for_third_column': images_for_third_column,
        'images_for_fourth_column': images_for_fourth_column,
    }

    return render(request, template_name, context)


def get_images_from_database(request):
    images_first_column_client_query = ImagesClient.objects.filter(client=request.user, column="First Column")
    images_second_column_client_query = ImagesClient.objects.filter(client=request.user, column="Second Column")
    images_third_column_client_query = ImagesClient.objects.filter(client=request.user, column="Third Column")
    images_fourth_column_client_query = ImagesClient.objects.filter(client=request.user, column="Fourth Column")
    return images_first_column_client_query, images_fourth_column_client_query, images_second_column_client_query, \
           images_third_column_client_query


@login_required
def personal_gallery_view(request):
    template_name = 'gallery/personal_gallery_view.html'

    images_first_column_client_query, images_fourth_column_client_query, images_second_column_client_query, \
    images_third_column_client_query = get_images_from_database(
        request)

    context = {
        'images_first_column_client_query': images_first_column_client_query,
        'images_second_column_client_query': images_second_column_client_query,
        'images_third_column_client_query': images_third_column_client_query,
        'images_fourth_column_client_query': images_fourth_column_client_query,
    }

    return render(request, template_name, context)


def choose_preferred_images_view(request):
    template_name = 'gallery_details/pick_images_from_gallery.html'

    images_first_column_client_query, images_fourth_column_client_query, images_second_column_client_query, \
    images_third_column_client_query = get_images_from_database(
        request)

    context = {
        'images_first_column_client_query': images_first_column_client_query,
        'images_second_column_client_query': images_second_column_client_query,
        'images_third_column_client_query': images_third_column_client_query,
        'images_fourth_column_client_query': images_fourth_column_client_query,
    }

    return render(request, template_name, context)


class ChoosePreferredPhotosDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
    model = ImagesClient
    template_name = 'gallery_details/personal_image_details.html'

    slug_field = 'image_slug'
    slug_url_kwarg = 'image_slug'

    form_class = ImageClientForm

    def get_success_url(self):
        return reverse('choose_preferred_photos')

    def get_context_data(self, **kwargs):
        context = super(ChoosePreferredPhotosDetailView, self).get_context_data(**kwargs)
        context['form'] = ImageClientForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.client = request.user

            return self.form_valid(form_obj)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ChoosePreferredPhotosDetailView, self).form_valid(form)
