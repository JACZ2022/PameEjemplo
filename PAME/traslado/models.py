from django.db import models
from catalogos.models import Estacion
from vigilancia.models import Extranjero, Proceso

# Create your models here.

class traslado(models.Model):
    numeroOficio = models.CharField(max_length=50)
    fechaOficio = models.DateTimeField()
    estacionOrigen = models.CharField(max_length=50)
    estacionDestino = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    estatus = models.CharField(max_length=50)
    numeroUnicoProceso = models.models.ForeignKey(Proceso,  on_delete=models.CASCADE)
