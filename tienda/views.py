from django.shortcuts import render
from tienda.models import Producto

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    productos = Producto.objects.all();
    return render(request, 'tienda/listado.html', {'productos':productos})

"""
Crear vista para detalle del producto. Pasarle Producto y pk

producto = get_object_or_404(Producto, pk=pk)

crear forms.py para hacer el formulario de edicion de producto

añadir vista para nuevo y eliminar
"""







