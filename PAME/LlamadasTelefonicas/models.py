from django.db import models
from vigilancia.models import Extranjero

class llamadaTelefonica(models.Model):
    estacionMigratoria = models.CharField(max_length=50)
    fechaLlamada = models.DateField()
    horaLlamada = models.DateTimeField()
    deseaLlamar = models.BooleanField()
    motivoNoLlamada =  models.TextField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    firmaExtranjero = models.CharField(max_length=100)
    huellaExtranjero = models.CharField(max_length=100)
    
    
    
# Create your models here.
