from django.contrib import admin

from .models import (
    AvailableJob,
    AvailableInternship,
    JobsAppliance,
    InternshipsAppliance,
)


class AvailableJobAdmin(admin.ModelAdmin):
    list_display = ('post', 'location', 'job_type', 'released_day')
    prepopulated_fields = {'job_slug': ('post',)}


class AvailableInternshipAdmin(admin.ModelAdmin):
    list_display = ('post', 'location', 'job_type', 'released_day')
    prepopulated_fields = {'internship_slug': ('post',)}


class JobsApplianceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'career', 'date', 'accepted')


class InternshipsApplianceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'career', 'date', 'accepted')


admin.site.register(AvailableJob, AvailableJobAdmin)
admin.site.register(AvailableInternship, AvailableInternshipAdmin)
admin.site.register(JobsAppliance, JobsApplianceAdmin)
admin.site.register(InternshipsAppliance, InternshipsApplianceAdmin)
