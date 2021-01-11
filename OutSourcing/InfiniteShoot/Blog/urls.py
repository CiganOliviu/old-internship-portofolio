from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='blog_view')
]
