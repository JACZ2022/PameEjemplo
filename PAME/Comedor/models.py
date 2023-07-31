from django.db import models
from vigilancia.models import Extranjero

# Create your models here.
class Dietas(models.Model):
    tipoDieta = models.CharField(max_length=50)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)



class Comedor(models.Model):
    fechaEvento = models.DateField()
    horaEvento = models.DateTimeField()
    comida = models.BooleanField()
    desayuno = models.BooleanField()
    cena = models.BooleanField()
    firmaExtranjero = models.BinaryField()
    huellaExtranjero = models.BinaryField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    

class BoxLunch(models.Model):
    fechaEvento = models.DateField()
    horaEvento = models.DateTimeField
    firmaResponsable = models.BinaryField()
    huellaResponsable=models.BinaryField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)