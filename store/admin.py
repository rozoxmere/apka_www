from django.contrib import admin

from store.models import Product, Osoba

# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko"]

admin.site.register(Product)
admin.site.register(Osoba,OsobaAdmin)