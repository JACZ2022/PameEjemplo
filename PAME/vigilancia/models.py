from django.db import models


# Create your models here.
class Extranjero(models.Model):
    fechaRegistro = models.DateField()
    horaRegistro = models.DateTimeField()
    numeroExtranjero = models.IntegerField()
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
    
    
class OficioPuestaDisposicionINM(models.Model):
    numeroOficio = models.IntegerField()
    fechaOficio = models.DateField()
    nombreAutoridadSigna = models.CharField(max_length=100)
    cargoAutoridadSigna = models.CharField(max_length=100)
    puntoRevision = models.CharField(max_length=100)
    oficioPuesta = models.BinaryField()
    oficioComision = models.BinaryField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
     
class OficioPuestaDisposicionAC(models.Model):
    numeroOficio = models.IntegerField()
    fechaOficio = models.DateField()
    dependencia = models.CharField(max_length=100)
    numeroCarpeta = models.CharField(max_length=30)
    nombreAutoridadSigna = models.CharField(max_length=100)
    cargoAutoridadSigna = models.CharField(max_length=100)
    entidadFederativa = models.CharField(max_length=100)
    oficioPuesta =models.BinaryField()
    certificadoMedico = models.BinaryField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    


class Acompanante(models.Model):
    delExtranjero = models.IntegerField()
    delAcompanante = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    relacion = models.CharField(max_length=30)
    
    

    
     