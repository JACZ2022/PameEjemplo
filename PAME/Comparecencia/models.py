from django.db import models
from vigilancia.models import Extranjero


# Create your models here.
class Comparecencia(models.Model):
    fechaComparecencia = models.DateField()
    horaComparecencia = models.DateTimeField()
    estadoCivil = models.CharField(max_length=50)
    escolaridad = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    lugarOrigen =models.CharField(max_length=50)
    calleDomicilioPais = models.CharField(max_length=50)
    numeroDomicilioPais = models.IntegerField()
    localidadPais = models.CharField(max_length=50)
    domicilioEnMexico = models.BooleanField()
    nombrePadre = models.CharField(max_length=50)
    apellidoPaternoPadre = models.CharField(max_length=50)
    apellidoMaternoPadre = models.CharField(max_length=50)
    nombreMadre = models.CharField(max_length=50)
    apellidoPaternoMadre = models.CharField(max_length=50)
    apellidoMaternoMadre = models.CharField(max_length=50)
    
    