from django.contrib import admin
from .models import PastEvent, SponsorEvent, HostEvent

class PastEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'location', 'space', 'part_of_event', 'date')
    prepopulated_fields = {'past_event_slug': ('event_name', )}

class SponsorEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'location', 'space', 'part_of_event', 'date')
    prepopulated_fields = {'event_slug' : ('event_name', )}

class HostEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'location', 'space', 'part_of_event', 'date')
    prepopulated_fields = {'event_slug' : ('event_name', )}

admin.site.register(PastEvent, PastEventAdmin)
admin.site.register(SponsorEvent, SponsorEventAdmin)
admin.site.register(HostEvent, HostEventAdmin)
