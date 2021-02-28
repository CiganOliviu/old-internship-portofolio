from django.contrib import admin
from .models import Newsletter, Contact


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'title', 'email', 'sent_date', 'read')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)

