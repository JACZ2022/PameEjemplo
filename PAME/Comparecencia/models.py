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
    designaRepresentanteLegal= models.BooleanField()
    nombreRepresentante = models.CharField(max_length=50)
    apellidoPaternoRepresentante = models.CharField(max_length=50)
    apellidoMaternoRepresentante = models.CharField(max_length=50)
    fechaIngresoMexico= models.DateField()
    lugarIngresoMexico= models.CharField(max_length=50)
    formaIngresoMexico= models.CharField(max_length=50)
    decalaracion= models.TextField()
    solicitaRefugio= models.BooleanField()
    victimaDelito= models.BooleanField()
    delExtranjero= models.ForeignKey(Extranjero, on_delete=models.CASCADE)


class Refugio(models.Model):
    notificacionComar= models.TextField()
    fechaNotificacion= models.DateField()
    delExtranjero= models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    contstanciaAdmisnion = models.CharField(max_length=100)
    acuerdoSuspension = models.CharField(max_length=100)
        
class VictimaDelito(models.Model):
    notificacionAutoridad = models.TextField()
    fechaNotificacion= models.DateField()
    delExtranjero= models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    documentoMigratorio = models.CharField(max_length=100)
    asunto = models.TextField()
    documentoFGR = models.CharField(max_length=100)

class Consular(models.Model):
    lugar= models.CharField(max_length=50)
    fechaNotificacionConsular= models.DateField()
    horaNotificacionConsular = models.DateTimeField()
    consulado= models.CharField(max_length=50)
    tipoResolucion = models.CharField(max_length=50)
    delExtranjero= models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    numeroOficio = models.CharField(max_length=50)
    asunto = models.TextField() 
    

    