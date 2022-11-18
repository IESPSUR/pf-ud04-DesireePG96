from django.forms import ModelForm, Form
from django import forms
from .models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class CompraForm(Form):
    unidades = forms.IntegerField(required=True, min_value=1)
