from django.contrib import admin
from .models import Marca, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "modelo", "unidades", "precio", "detalles", "marca")

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)


