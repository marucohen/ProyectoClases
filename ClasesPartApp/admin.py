from django.contrib import admin
from .models import ClasesPart

# Register your models here.
class ClasesPartAppAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(ClasesPart, ClasesPartAppAdmin)
