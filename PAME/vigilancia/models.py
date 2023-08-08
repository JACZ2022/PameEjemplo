from django.db import models
from Generales.models import EstacionMigratoria



# Create your models here.
class TipoDisposicion(models.Model):
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    



class PuestaDisposicion(models.Model):
    numeroOficio = models.CharField(max_length=50)
    fechaOficio = models.DateField()
    nombreAutoridadSigna = models.CharField(max_length=100)
    cargoAutoridadSigna = models.CharField(max_length=100)
    oficioPuesta = models.BinaryField()
    oficioComision = models.BinaryField()
    deLaEstacion = models.ForeignKey(EstacionMigratoria, on_delete=models.CASCADE)
    deLadisposicion = models.ForeignKey(TipoDisposicion, on_delete=models.CASCADE)
   

class Extranjero(models.Model):
    fechaRegistro = models.DateField()
    horaRegistro = models.DateTimeField()
    numeroExtranjero = models.IntegerField()
    estacionMigratoria = models.CharField(max_length=50)
    nombreExtranjero = models.CharField(max_length= 50)
    apellidoPaternoExtranjero = models.CharField(max_length=50)
    apellidoMaternoExtranjero = models.CharField(max_length=50)
    firmaExtranjero = models.BinaryField()
    huellaExtranjero = models.BinaryField()
    nacionalidad = models.CharField(max_length=50)
    genero = models.CharField(max_length= 10)
    fechaNacimiento = models.DateField()
    documentoIdentidad = models.BinaryField()
    fotografiaExtranjero = models.BinaryField()
    viajaSolo = models.BooleanField()
    tipoEstancia = models.CharField(max_length=50)
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)
    

    
class ComplementoINM(models.Model):
    puntoRevision = models.CharField(max_length=100)
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)
    
 
    
     
class ComplementonAC(models.Model):
    dependencia = models.CharField(max_length=100)
    numeroCarpeta = models.CharField(max_length=30)
    entidadFederativa = models.CharField(max_length=100)
    certificadoMedico = models.BinaryField()
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)
    
class ComplementoTraslado(models.Model):
    estacionOrigen = models.CharField(max_length=100)
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)

class ComplementoPorTrasladar(models.Model):
    estacionDestino = models.CharField(max_length=100)
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)
    
    
class complementoAlojamiento(models.Model):
    estacionOrigen = models.CharField(max_length=100)
    deLaPuesta = models.ForeignKey(PuestaDisposicion, on_delete= models.CASCADE)

class Acompanante(models.Model):
    delExtranjero = models.IntegerField()
    delAcompanante = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    relacion = models.CharField(max_length=30)
    
    

    
     