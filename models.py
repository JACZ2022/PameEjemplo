from django.db import models
from catalogos.models import Estacion
from vigilancia.models import Extranjero, Proceso

# Create your models here.

OPCION_STATUS_CHOICES=[
    [0,'SOLICITUD'],
    [1,'ACEPTADO'],
    [2,'RECHAZADO'],
]

OPCION_STATUS_TRASLADO_CHOICES=[
    [0,'ACPTADO'],
    [1,'RECHAZADO'],
]

class Traslado(models.Model):
    numeroUnicoProceso = models.CharField(max_length=50)
    estacionOrigen = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    estacionDestino = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    fechaSolicitud = models.DateTimeField()
    fechaAceptacion = models.DateTimeField()
    fechaTraslado = models.DateTimeField()
    fechaArrivo = models.DateTimeField()
    nombreAutoridadEnvia = models.CharField(max_length=100)
    nombreAutoridadRecibe = models.CharField(max_length=100)
    responsableEnvia = models.CharField(max_length=100)
    responsableRecibe = models.CharField(max_length=100)
    enTraslado = models.BooleanField()
    status = models.IntegerField(choices=OPCION_STATUS_CHOICES)
    
class ExtranjeroTraslado(models.Model):
    statusTraslado = models.IntegerField(choices=OPCION_STATUS_TRASLADO_CHOICES)
    delTraslado = models.ForeignKey(Traslado, on_delete=models.CASCADE, null=True, blank=True)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE, null=True, blank=True)


class Alojamiento(models.Model):
    numeroOficio = models.CharField(max_length=50)
    fechaOficio = models.DateTimeField()
    estacionOrigen = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    estacionDestino = models.CharField(max_length=50)
    estatus = models.CharField(max_length=50)
    numeroUnicoProceso = models.ForeignKey(Proceso,  on_delete=models.CASCADE)
    acuerdoTraslado = models.FileField(upload_to='files/', null=True, blank=True)
