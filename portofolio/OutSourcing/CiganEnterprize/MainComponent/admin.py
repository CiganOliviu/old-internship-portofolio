from django.contrib import admin

from .models import Studio


class StudioAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'country', 'moment')
    prepopulated_fields = {'studio_slug': ('city',)}


admin.site.register(Studio, StudioAdmin)
