from django.db import models
from vigilancia.models import Extranjero

class llamadaTelefonica(models.Model):
    estacionMigratoria = models.CharField(max_length=50)
    fechaLlamada = models.DateField()
    horaLlamada = models.DateTimeField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    firmaExtranjero = models.CharField(max_length=100)
    huellaExtranjero = models.CharField(max_length=100)
    
class Notificacion(models.Model):
    fechaNotificacion = models.DateField()
    horaNotificacion = models.DateTimeField()
    deseaLlamar = models.BooleanField()
    motivoNoLlamada =  models.TextField()
    firmaExtranjero = models.CharField(max_length=100)
    huellaExtranjero = models.CharField(max_length=100)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)

