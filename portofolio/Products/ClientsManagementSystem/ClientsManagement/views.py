from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    template_name = 'views/client_index_view.html'

    return render(request, template_name)
