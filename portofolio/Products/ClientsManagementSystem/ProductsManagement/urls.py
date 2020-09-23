from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_handler, name = 'product_handler'),
]
