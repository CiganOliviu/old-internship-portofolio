from django.contrib import admin
from .models import ImagesClient, PlatformPresentationImage


class PlatformPresentationImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'column')


class ImagesClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'column')
    prepopulated_fields = {'image_slug': ('name', )}


admin.site.register(PlatformPresentationImage, PlatformPresentationImageAdmin)
admin.site.register(ImagesClient, ImagesClientAdmin)
