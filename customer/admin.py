from django.contrib import admin
from .models import CustomerContact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'subject',)

    search_fields = ('full_name', 'email')

admin.site.register(CustomerContact, ContactAdmin)
