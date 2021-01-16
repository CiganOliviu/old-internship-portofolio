from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog_view'),
    path('blog/results/', views.blog_posts_search_view, name='blog_view_results'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
]
