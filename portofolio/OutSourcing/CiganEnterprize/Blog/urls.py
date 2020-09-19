from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog_name'),
    path('blog/results/', views.blog_posts_search_view, name='blog_search'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
