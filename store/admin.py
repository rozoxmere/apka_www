from django.contrib import admin

from store.models import Product, Osoba, Druzyna

# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko", "druzyna", "data_dodania"]
    list_filter = ("druzyna" , "data_dodania")


class DruzynaAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "kraj"]


admin.site.register(Product)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)