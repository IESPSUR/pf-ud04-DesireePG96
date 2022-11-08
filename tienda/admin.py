from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Marca, Producto, Compra
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Compra)


