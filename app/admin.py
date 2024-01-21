from django.contrib import admin
from .models import Abonent, News


class AbonentAdmin(admin.ModelAdmin):
    list_display = ("name_abonent", "number", "tarif", "balance", "min", 
                    "sms", "in_min","vne_min", "in_sms", "internet")

class NewAdmin(admin.ModelAdmin):
    list_display = ("title", 'date', 'full', 'img')


admin.site.register(Abonent, AbonentAdmin)
admin.site.register(News, NewAdmin)


