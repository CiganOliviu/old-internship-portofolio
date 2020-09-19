from django.contrib import admin
from .models import NewsLetter, Contact

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'title', 'email', 'sent_date')

admin.site.register(NewsLetter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
