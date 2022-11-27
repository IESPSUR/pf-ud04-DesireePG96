from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto, Marca, Compra
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

"""
Vista para la visualizacion del listado de productos
"""
def listado(request):
    productos = Producto.objects.all();
    return render(request, 'tienda/listado.html', {'productos':productos})

"""
Vista para la creacion de nuevo producto
"""
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

"""
Vista para la edicion de producto
"""
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

"""
Vista para la eliminacion de producto
"""
def eliminar(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':

        producto.delete()
        return redirect('listado')

    return render(request, 'tienda/eliminar.html', {'producto': producto})

"""
Vista para buscar el producto en la pagina de compra
"""
def compra(request):
    productos = Producto.objects.all();
    busqueda = request.GET.get('datoBusqueda')

    if busqueda:
        productos = productos.filter(nombre__icontains = busqueda)

    return render(request, 'tienda/compra.html', {'productos':productos})

"""
Vista para el carrito
"""
def checkout(request, pk):

    producto = get_object_or_404(Producto, pk=pk)
    unidades = request.GET.get('unidades')
    total = producto.precio * int(unidades)

    if request.method == 'POST':
        if producto.unidades < int(unidades):
            return redirect('error')
        else:
            unidRestante = producto.unidades - int(unidades)
            producto.unidades = unidRestante
            producto.save()
            compra = Compra(producto = producto,
                            user = request.user,
                            fecha = datetime.today().strftime('%Y-%m-%d'),
                            unidades = unidades,
                            importe = total)
            compra.save()
            return redirect('compra')

    return render(request, 'tienda/checkout.html', {'producto':producto, 'unidades': unidades, 'total':total})

"""
Vista para el error de unidades
"""
def error(request):

    return render(request,'tienda/errorUnidades.html')

"""
Vista para el template de seleccion de informes
"""
@user_passes_test(lambda u: u.is_superuser)
def informes(request):

    return render(request,'tienda/informes.html')

"""
Vista para informe de productos por marcas
"""
@user_passes_test(lambda u: u.is_superuser)
def informeMarca(request):
    marcas = Marca.objects.all()
    productos = Producto.objects.all();
    busqueda = request.GET.get('datoBusqueda')

    if busqueda:
        productos = productos.filter(marca__nombre=busqueda)

    return render(request, 'tienda/productosMarca.html', {'marcas':marcas, 'productos': productos})

"""
Vista para el informe de compras de un usuario
"""
@user_passes_test(lambda u: u.is_superuser)
def compraUsuario(request):
    usuario = User.objects.all()
    compras = Compra.objects.all()
    busqueda = request.GET.get('datoBusqueda')

    if busqueda:
        compras = compras.filter(user=busqueda)

    return render(request,'tienda/compraUsuario.html', {'compras':compras, 'usuario':usuario})

"""
Vista para el top 10 productos mas vendidos
"""
@user_passes_test(lambda u: u.is_superuser)
def topProductos(request):
    productos = Producto.objects.all()
    compras = Compra.objects.all().values('producto_id').annotate(cantidad=Sum('unidades')).order_by('-cantidad')[:10]

    return render(request,'tienda/topProductos.html', {'productos':productos, 'compras':compras})

"""
Vista para el top 10 mejores clientes
"""
@user_passes_test(lambda u: u.is_superuser)
def topClientes(request):
    clientes = User.objects.all()
    compras = Compra.objects.all().values('user').annotate(importeTotal=Sum('importe'))[:10]

    return render(request,'tienda/topClientes.html', {'clientes':clientes, 'compras':compras})








