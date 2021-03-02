from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('personal-gallery/', views.personal_gallery_view, name='personal_gallery_view'),
    path('choose-preferred-photos/', views.choose_preferred_images_view, name='choose_preferred_photos'),
    path('personal-gallery/<slug:image_slug>/', views.ChoosePreferredPhotosDetailView.as_view(),
         name='choose_preferred_photos_detail_view'),
    path('my-catalogue/', views.my_catalogue, name='my_catalogue'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()