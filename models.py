from django.db import models
from catalogos.models import Estacion
from vigilancia.models import Extranjero, Proceso

# Create your models here.

class traslado(models.Model):
    numeroOficio = models.CharField(max_length=50)
    fechaOficio = models.DateTimeField()
    nombreAutoridadSigna = models.CharField(max_length=100)
    cargoAutoridadSigna = models.CharField(max_length=100)
    fechaTraslado = models.DateTimeField()
    fechaArrivo = models.DateTimeField()
    estacionOrigen = models.CharField(max_length=50)
    estacionDestino = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    estatus = models.CharField(max_length=50)
    numeroUnicoProceso = models.ForeignKey(Proceso,  on_delete=models.CASCADE)


class Alojamiento(models.Model):
    numeroOficio = models.CharField(max_length=50)
    fechaOficio = models.DateTimeField()
    estacionOrigen = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    estacionDestino = models.CharField(max_length=50)
    estatus = models.CharField(max_length=50)
    numeroUnicoProceso = models.ForeignKey(Proceso,  on_delete=models.CASCADE)
    acuerdoTraslado = models.FileField(upload_to='files/', null=True, blank=True)
