from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    fields =('name_shop', 'adr_shop')
    list_display = [ "name_shop", "adr_shop"]  # Выводит 3 поля
    search_fields = ( 'name_shop', 'adr_shop')
    list_filter = ["id_shop"]                                                            # Фильтр по поляи
    class Meta:
        model = Shop

class TovarAdmin(admin.ModelAdmin):
    fields = ('name_tovar', 'type_tovar')
    list_display = [ "name_tovar", "type_tovar"]  # Выводит 3 поля
    search_fields = ('name_tovar', 'type_tovar')
    list_filter = ["id_tovar"]
    class Meta:
        model = Tovar

class WorkerAdmin(admin.ModelAdmin):
    fields = ('name_worker', 'lastname_worker', 'email_worker', 'workplace_worker')
    list_display = ["name_worker", "lastname_worker", "email_worker"]  # Выводит 3 поля
    search_fields = ('name_worker', 'lastname_worker', 'email_worker', 'workplace_worker')
    list_filter = ["id_worker"]
    class Meta:
        model = Worker


admin.site.register(Shop, ShopAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Worker, WorkerAdmin)
