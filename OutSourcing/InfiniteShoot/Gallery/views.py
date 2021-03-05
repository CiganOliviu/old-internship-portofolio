from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from .models import *
from Gallery.form import ClientCatalogueForm


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

    form_class = ClientCatalogueForm

    def get_success_url(self):

        return reverse('choose_preferred_photos')

    def get_context_data(self, **kwargs):
        context = super(ChoosePreferredPhotosDetailView, self).get_context_data(**kwargs)
        context['form'] = ClientCatalogueForm(initial={'post': self.object})

        return context

    def get_number_of_instances_from_database(self, database_name, filter_name):

        return database_name.objects.filter(image_positioning=filter_name).count()

    def validate_query(self, database_name, filter_name):

        if filter_name == "Cover Image":
            if self.get_number_of_instances_from_database(database_name, "Cover Image") == 1:
                return False

        if filter_name == "Content Image":
            if self.get_number_of_instances_from_database(database_name, "Content Image") == 4:
                return False

        if filter_name == "Back Image":
            if self.get_number_of_instances_from_database(database_name, "Back Image") == 1:
                return False

        return True

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.client = request.user

            form_obj.image = self.__get_specific_image(request.user, self.kwargs['image_slug']).image

            if self.validate_query(ClientCatalogue, form_obj.image_positioning):
                return self.form_valid(form_obj)

            return self.form_invalid(form)

        else:
            return self.form_invalid(form)

    @staticmethod
    def __get_specific_image(user, name_id):
        result = ImagesClient.objects.get(client=user, name=name_id)

        return result

    def form_valid(self, form):
        form.save()

        return super(ChoosePreferredPhotosDetailView, self).form_valid(form)


def my_catalogue(request):
    template_name = 'gallery_details/my_catalogue.html'

    get_cover_image = ClientCatalogue.objects.filter(client=request.user, image_positioning='Cover Image')
    get_image = ClientCatalogue.objects.filter(client=request.user, image_positioning='Content Image')
    get_back_image = ClientCatalogue.objects.filter(client=request.user, image_positioning='Back Image')

    context = {
        'get_cover_image': get_cover_image,
        'get_image': get_image,
        'get_back_image': get_back_image,
    }

    return render(request, template_name, context)
