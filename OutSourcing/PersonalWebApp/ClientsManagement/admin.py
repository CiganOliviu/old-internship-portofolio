from django.contrib import admin

from ClientsManagement.models import (
    ClientsFeedBack,
    ProjectsRequest,
    MessagesToClient,
    ClientsDetail,

)


class ClientsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date')


class ProjectsRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date', 'project_status')


class MessagesToClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'subject', 'type_of_message', 'date')
    prepopulated_fields = {'message_slug': ('title',)}


class ClientsDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_of_client', 'number_of_projects_in_progress',
                    'number_of_proposed_projects', 'number_of_finished_projects',)


admin.site.register(ClientsFeedBack, ClientsFeedbackAdmin)
admin.site.register(ProjectsRequest, ProjectsRequestAdmin)
admin.site.register(MessagesToClient, MessagesToClientAdmin)
admin.site.register(ClientsDetail, ClientsDetailAdmin)
