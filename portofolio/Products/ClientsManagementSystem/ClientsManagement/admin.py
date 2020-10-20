from django.contrib import admin

from ClientsManagement.models import (
    FeedBack,
    AskProject,
    DirectClientContact,
    ClientInfo,
)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date')

class AskProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'type', 'date')

class DirectClientContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date')

class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_of_client', 'number_of_finalised_projects', 'number_of_proposed_projects')

admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(AskProject, AskProjectAdmin)
admin.site.register(DirectClientContact, DirectClientContactAdmin)
admin.site.register(ClientInfo, ClientInfoAdmin)
