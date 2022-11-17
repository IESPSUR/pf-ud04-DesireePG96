from django.urls import path
from . import views

urlpatterns = [
    path('tienda/admin/listado/', views.listado, name='listado'),
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/editar/<int:pk>', views.editar, name='editar'),
    path('tienda/admin/nuevo', views.nuevo, name='nuevo')
]
