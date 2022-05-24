from django.contrib import admin
from main.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'number_of_telephone', 'message', 'sent_at']
    list_filter = ['sent_at']
    search_fields = ['email', 'number_of_telephone', 'message', 'sent_at']
    list_editable = ['number_of_telephone']
# Register your models here.
admin.site.register(Contact, ContactAdmin)