from django.urls import path
from . import views, admin

urlpatterns = [
    path('tienda/admin/listado/', views.listado, name='listado'),
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
]
