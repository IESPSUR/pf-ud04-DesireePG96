from django.urls import path
from . import views

urlpatterns = [
    path('tienda/informes/topClientes', views.topClientes, name='topClientes'),
    path('tienda/informes/topProductos', views.topProductos, name='topProductos'),
    path('tienda/informes/compraUsuario', views.compraUsuario, name='compraUsuario'),
    path('tienda/informes/marca', views.informeMarca, name='porMarca'),
    path('tienda/informes', views.informes, name='informes'),
    path('tienda/checkout/error', views.error, name='error'),
    path('tienda/checkout/<int:pk>', views.checkout, name='checkout'),
    path('tienda/compra', views.compra, name='compra'),
    path('tienda/admin/listado/', views.listado, name='listado'),
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/eliminar/<int:pk>', views.eliminar, name='eliminar'),
    path('tienda/admin/editar/<int:pk>', views.editar, name='editar'),
    path('tienda/admin/nuevo', views.nuevo, name='nuevo')
]
