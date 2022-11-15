from django.shortcuts import render, redirect
from tienda.models import Producto
from .forms import ProductoForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    productos = Producto.objects.all();
    return render(request, 'tienda/listado.html', {'productos':productos})


def nuevo(request):
    form = ProductoForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():

            producto = Producto(nombre=form.cleaned_data['nombre'],
                                modelo=form.cleaned_data['modelo'],
                                unidades=form.cleaned_data['unidades'],
                                precio=form.cleaned_data['precio'],
                                detalle=form.cleaned_data['detalle'],
                                marca=form.cleaned_data['marca'])
            producto.save()

            return redirect('listado')

        else:
            form = ProductoForm()
            return redirect('listado')

    return render(request, 'tienda/nuevo.html', {'form':form})



"""
Crear vista para detalle del producto. Pasarle Producto y pk

producto = get_object_or_404(Producto, pk=pk)

crear forms.py para hacer el formulario de edicion de producto

añadir vista para nuevo y eliminar

"""
def editar(request, pk):
    return render(request, 'tienda/editar.html')

"""
Pasos para realizar la compra:

crear formulario compra en forms para las unidades

en vistas crear tienda productos (coge los productos y crea el compra form vacio renderizado con un template, parecido al de gestion de productos)

transacciones de forma atomica
vista de checkout
"""







