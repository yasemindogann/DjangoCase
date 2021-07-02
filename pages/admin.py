from django.contrib import admin
from . models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'email', 'link', 'aciklama', 'code') # tablodaki stunlar
    search_fields = ('baslik', 'email', 'link', 'aciklama') #tablodaki aranabilir alanlar

admin.site.register(Contact, ContactAdmin)
