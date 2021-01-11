from django.shortcuts import render


def contact_view(request):
    template_name = 'contact/contact_view.html'

    return render(request, template_name)


def newsletter_view(request):
    template_name = 'newsletter/newsletter_view.html'

    return render(request, template_name)