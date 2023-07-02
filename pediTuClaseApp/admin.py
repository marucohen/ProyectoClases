from django.contrib import admin
from .models import CategoriaClase, ClaseProducto

# Register your models here.
class CategoriaClaseAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ClaseProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(CategoriaClase, CategoriaClaseAdmin)
admin.site.register(ClaseProducto, ClaseProductoAdmin)