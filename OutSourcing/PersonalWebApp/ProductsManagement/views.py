from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import FinishedProduct, ActiveWorkingProduct, PlannedProduct

from .products_administration import (
    save_product_from_active_products_in_finished_products,
    save_product_from_planned_products_in_active_products,
)


@login_required
def products_handler(request):

    template_name = 'views/products.html'

    active_product_query = ActiveWorkingProduct.objects.all()
    finished_product_query = FinishedProduct.objects.all()
    planned_product_query = PlannedProduct.objects.all()

    context = {
        'active_product_query': active_product_query,
        'finished_product_query': finished_product_query,
        'planned_product_query': planned_product_query,
    }

    save_product_from_planned_products_in_active_products()
    save_product_from_active_products_in_finished_products()

    return render(request, template_name, context)


class PlannedProductDetail(LoginRequiredMixin, generic.DetailView):

    model = PlannedProduct

    template_name = 'views/products_detail/planned_product_detail.html'

    slug_field = 'planned_product_slug'
    slug_url_kwarg = 'planned_product_slug'


class FinishedProductDetail(LoginRequiredMixin, generic.DetailView):

    model = FinishedProduct

    template_name = 'views/products_detail/finished_product_detail.html'

    slug_field = 'finished_product_slug'
    slug_url_kwarg = 'finished_product_slug'


class ActiveWorkingProductDetail(LoginRequiredMixin, generic.DetailView):

    model = ActiveWorkingProduct

    template_name = 'views/products_detail/active_working_product_detail.html'

    slug_field = 'active_working_product_slug'
    slug_url_kwarg = 'active_working_product_slug'

