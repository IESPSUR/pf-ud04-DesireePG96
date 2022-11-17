from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto
from .forms import ProductoForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    productos = Producto.objects.all();
    return render(request, 'tienda/listado.html', {'productos':productos})

def nuevo(request):
    form = ProductoForm(request.POST or None)

    if request.method == 'POST':
        print(form.is_valid(), form.errors)
        if form.is_valid():

            producto = Producto(nombre=form.cleaned_data['nombre'],
                                modelo=form.cleaned_data['modelo'],
                                unidades=form.cleaned_data['unidades'],
                                precio=form.cleaned_data['precio'],
                                detalles=form.cleaned_data['detalles'],
                                marca=form.cleaned_data['marca'])
            producto.save()

            return redirect('listado')

        else:
            return redirect('listado')

    return render(request, 'tienda/nuevo.html', {'form':form})

def editar(request, pk):

    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST':
        print(form.is_valid(), form.errors)
        if form.is_valid():
            form.save()

            return redirect('listado')

        else:
            return redirect('listado')

    return render(request, 'tienda/editar.html', {'form': form, 'producto': producto})

def eliminar(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':

        producto.delete()
        return redirect('listado')

    return render(request, 'tienda/eliminar.html', {'producto': producto})



"""
Pasos para realizar la compra:

crear formulario compra en forms para las unidades

en vistas crear tienda productos (coge los productos y crea el compra form vacio renderizado con un template, parecido al de gestion de productos)

transacciones de forma atomica
vista de checkout
"""

def compra(request):
    productos = Producto.objects.all();
    busqueda = request.GET.get('datoBusqueda')
    unidades = request.POST.get('unidades')

    if busqueda:
        encontrado = productos.filter(nombre__icontains = busqueda)
        return render(request, 'tienda/compra.html', {'productos': encontrado})

    if request.method == 'POST':
        return render(request, 'tienda/checkout.html', {'unidades':unidades, })



    return render(request, 'tienda/compra.html', {'productos':productos})

def checkout(request, pk):

    producto = get_object_or_404(Producto, pk=pk)
    unidades = request.GET.get('unidades')
    print(unidades)
    print(type(unidades))
    total = float(unidades) * float(producto.precio);

    if request.method == 'POST':

        unidRestante = producto.unidades - unidades
        producto.unidades = unidRestante
        producto.save()
        return redirect('compra')

    return render(request, 'tienda/checkout.html', {'producto':producto, 'unidades':unidades, 'total':total})







