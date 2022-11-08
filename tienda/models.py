from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    modelo = models.CharField(max_length=30)
    unidades = models.IntegerField
    precio = models.FloatField
    detalles = models.CharField(max_length=500)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Compra(models.Model):
    fecha = models.DateField
    unidades = models.IntegerField
    importe = models.FloatField
    nombre = models.ForeignKey(Producto, on_delete=models.CASCADE)




