from django.db import models
from vigilancia.models import Extranjero

class llamadaTelefonica(models.Model):
    estacionMigratoria = models.CharField(max_length=50)
    fechaLlamada = models.DateField()
    horaLlamada = models.DateTimeField()
    deseaLlamar = models.BooleanField()
    motivoNoLlamada =  models.TextField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    
    
# Create your models here.
