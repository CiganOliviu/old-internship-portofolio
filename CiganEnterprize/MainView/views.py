from django.shortcuts import render

def index(request):

    template_name = 'views/index.html'
    
    return render(request, template_name)
