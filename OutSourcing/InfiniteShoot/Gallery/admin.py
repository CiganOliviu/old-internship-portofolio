from django.contrib import admin
from .models import ImagesClient, PlatformPresentationImage, ClientCatalogue


class PlatformPresentationImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'column')


class ImagesClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'column')
    prepopulated_fields = {'image_slug': ('name', )}


class ClientCatalogueAdmin(admin.ModelAdmin):
    list_display = ('client', 'image_positioning')

admin.site.register(PlatformPresentationImage, PlatformPresentationImageAdmin)
admin.site.register(ImagesClient, ImagesClientAdmin)
admin.site.register(ClientCatalogue, ClientCatalogueAdmin)