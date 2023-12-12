from django.contrib import admin
from django.utils.html import mark_safe

from tienda.models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "precio", "coleccion", "ver_foto"]

    def ver_foto(self, obj):
        try:
            return mark_safe(f"<img src='{obj.foto.url}' width='10%'>")
        except Exception as e:
            return f"Error, el archivo fue eliminado."

class UsusarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombreCompleto", "email", "password", "rol"]

    def nombreCompleto(self, obj):
        return mark_safe(f"{obj.nombre} {obj.apellido}")
    
admin.site.register(Productos, ProductoAdmin)
admin.site.register(Usuarios, UsusarioAdmin)