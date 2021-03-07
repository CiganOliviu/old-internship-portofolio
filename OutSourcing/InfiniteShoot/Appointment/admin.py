from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'desired_date', 'sent_moment', 'seen', 'accepted')


admin.site.register(Appointment, AppointmentAdmin)
