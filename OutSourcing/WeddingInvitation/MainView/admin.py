from django.contrib import admin
from .models import ConfirmAnswer, GuestEnvironmentDetail


class ConfirmAnswerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'submitted', 'answer_sent')

    def user_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name


admin.site.register(ConfirmAnswer, ConfirmAnswerAdmin)
admin.site.register(GuestEnvironmentDetail)

admin.site.site_header = "Wedding Invitation Administration Website"
