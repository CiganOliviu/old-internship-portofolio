from django.shortcuts import render


def gallery_view(request):
    template_name = 'gallery/gallery_view.html'

    return render(request, template_name)

