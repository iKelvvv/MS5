from django.contrib import admin
from .models import CustomerContact, NewletterSubscriber


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'subject',)

    search_fields = ('full_name', 'email')


class SubscribersAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date',)

    search_fields = ('email', 'date',)


admin.site.register(NewletterSubscriber, SubscribersAdmin)
admin.site.register(CustomerContact, ContactAdmin)
