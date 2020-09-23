from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import FinishedProduct, ActiveWorkingProduct

@login_required
def products_handler(request):

    template_name = 'views/products.html'

    active_product_query = ActiveWorkingProduct.objects.all()
    finished_product_query = FinishedProduct.objects.all()

    context = {
        'active_product_query' : active_product_query,
        'finished_product_query' : finished_product_query,
    }

    return render(request, template_name)
