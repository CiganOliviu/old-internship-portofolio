from django.contrib import admin

from .models import (
    AvaibleJob,
    Studio,
    JobsAppliance,
    AvaibleInternship,
    InternshipsAppliance
)

class StudioAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'country', 'moment')
    prepopulated_fields = {'studio_slug': ('city',)}

class AvaibleJobAdmin(admin.ModelAdmin):
    list_display = ('post', 'location', 'job_type', 'released_day')
    prepopulated_fields = {'job_slug': ('post',)}

class AvaibleInternshipAdmin(admin.ModelAdmin):
    list_display = ('post', 'location', 'released_day')
    prepopulated_fields = {'internship_slug': ('post',)}

class JobsApplianceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'carrer', 'date')

class InternshipsApplianceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'carrer', 'date')

admin.site.register(Studio, StudioAdmin)
admin.site.register(AvaibleJob, AvaibleJobAdmin)
admin.site.register(AvaibleInternship, AvaibleInternshipAdmin)
admin.site.register(JobsAppliance, JobsApplianceAdmin)
admin.site.register(InternshipsAppliance, InternshipsApplianceAdmin)
