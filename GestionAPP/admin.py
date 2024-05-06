from django.contrib import admin
from GestionAPP.models import Lugares as Lugar,Transporte,Excursiones as Excursion,Clientes
# Register your models here.

class LugarAdmin(admin.ModelAdmin):
    list_display = ("nombre","picture",)
    search_fields = ("nombre",)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ("marca","modelo","nombre_propietario","nombre_propietario","apellido_propietario","cuit_propietario")
    search_fields = ("marca","modelo","nombre_propietario","apellido_propietario","cuil_propietario")
    list_filter = ("marca","cuit_propietario")

class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("lugar","precio")
    search_fields = ("lugar","precio")
    list_filter = ("lugar","precio")

admin.site.register(Lugar,LugarAdmin)
admin.site.register(Transporte,TransporteAdmin)
admin.site.register(Excursion,ExcursionAdmin)
admin.site.register(Clientes)