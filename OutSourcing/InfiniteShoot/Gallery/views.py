from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ImagesClient, PlatformPresentationImage


def gallery_view(request):
    template_name = "gallery/gallery_view.html"

    images_for_platform = PlatformPresentationImage.objects.all()

    context = {
        'images_for_platform': images_for_platform
    }

    return render(request, template_name, context)


@login_required
def personal_gallery_view(request):
    template_name = 'gallery/personal_gallery_view.html'

    images_clients_query = ImagesClient.objects.filter(client=request.user)

    context = {
        'images_clients_query': images_clients_query
    }

    return render(request, template_name, context)

