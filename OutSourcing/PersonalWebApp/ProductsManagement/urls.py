from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_handler, name='product_handler'),
    
    path('active-working-product-detail/<slug:active_working_product_slug>/',
         views.ActiveWorkingProductDetail.as_view(),
         name='active_working_product_detail'),

    path('planned-product-detail/<slug:planned_product_slug>/', views.PlannedProductDetail.as_view(),
         name='planned_product_detail'),

    path('finished-product-detail/<slug:finished_product_slug>/', views.FinishedProductDetail.as_view(),
         name='finished_product_detail'),
]
