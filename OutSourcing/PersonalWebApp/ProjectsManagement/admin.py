from django.contrib import admin

from .models import (
    FinishedProject,
    ActiveWorkingProject,
    PlannedProject,
)


class FinishedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'price')


class ActiveWorkingProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'percent_done', 'date', 'price', 'deadline')


class PlannedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'price', 'deadline_for_production', 'working_status')


admin.site.register(FinishedProject, FinishedProjectAdmin)
admin.site.register(ActiveWorkingProject, ActiveWorkingProjectAdmin)
admin.site.register(PlannedProject, PlannedProjectAdmin)
