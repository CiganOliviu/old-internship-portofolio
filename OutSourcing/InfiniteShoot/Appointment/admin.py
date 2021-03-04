from django.contrib import admin
from .models import Appointment, AdminResponse


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'desired_date', 'sent_moment')


class AdminResponseAdmin(admin.ModelAdmin):
    list_display = ('client', 'appointment', 'location', 'response_moment')


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AdminResponse, AdminResponseAdmin)
