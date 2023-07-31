from django.db import models
from vigilancia.models import Extranjero
# Create your models here.

class Inventario(models.Model):
    unidadMigratoria = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    horaEntrega = models.DateTimeField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)

class Pertenencias(models.Model):
    descripcion = models.DateField(max_length=100)
    cantidad = models.FloatField()
    Obsevaciones = models.CharField(max_length=100)
    delInventario =models.ForeignKey(Inventario, on_delete=models.CASCADE)
    
class Valores(models.Model):
    descripcion = models.DateField(max_length=100)
    cantidad = models.FloatField()
    Obsevaciones = models.CharField(max_length=100)
    delInventario =models.ForeignKey(Inventario, on_delete=models.CASCADE)