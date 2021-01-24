from django.contrib import admin
from .models import ImagesClient, PlatformPresentationImage


class PlatformPresentationImageAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ImagesClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'name')


admin.site.register(PlatformPresentationImage, PlatformPresentationImageAdmin)
admin.site.register(ImagesClient, ImagesClientAdmin)

