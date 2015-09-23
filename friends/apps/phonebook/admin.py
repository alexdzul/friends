from django.contrib import admin
from friends.apps.phonebook.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_filter = ('last_name', )
    search_fields = ['first_name', 'last_name']
