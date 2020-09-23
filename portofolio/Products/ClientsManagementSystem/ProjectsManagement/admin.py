from django.contrib import admin

from .models import (
    FinishedProject,
    ActiveWorkingProject,
    PlannedProject,
)

class FinishedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'price')

class ActiveWorkingProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'price')

class PlannedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'price')

admin.site.register(FinishedProject, FinishedProjectAdmin)
admin.site.register(ActiveWorkingProject, ActiveWorkingProjectAdmin)
admin.site.register(PlannedProject, PlannedProjectAdmin)
