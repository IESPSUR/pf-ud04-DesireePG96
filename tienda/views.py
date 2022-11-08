from django.shortcuts import render
from tienda.models import Producto

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    return render(request, 'tienda/listado.html', {})



def book_list(request):
    productos = Producto.objects.order_by('nombre')
    return render('listado.html', {'productos': productos})


