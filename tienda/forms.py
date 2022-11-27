from django.forms import ModelForm, Form
from django import forms
from .models import Producto
"""
Formulario con todos los atributos de producto
"""
class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
