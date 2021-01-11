from django.shortcuts import render


def blog_view(request):
    template_name = 'blog/blog_view.html'

    return render(request, template_name)

