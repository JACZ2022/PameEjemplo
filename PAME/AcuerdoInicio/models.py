from django.db import models
from vigilancia.models import Extranjero

# Create your models here.
class TestigoUno (models.Model):
    nombreTestigoUno = models.CharField(max_length=50)
    apellidoPaternoTestigoUno = models.CharField(max_length=50)
    apellidoMaternoTestigoUno = models.CharField(max_length=50)
    firmaTestigoUno = models.BinaryField()
    huellaTestigoUno = models.BinaryField()
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)

class TestigoDos (models.Model):
    nombreTestigoDos = models.CharField(max_length=50)
    apellidoPaternoTestigoDos = models.CharField(max_length=50)
    apellidoMaternoTestigoDos = models.CharField(max_length=50)
    firmaTestigoDos = models.BinaryField()
    huellaTestigoDos = models.BinaryField()
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    
class Traductor (models.Model):
    nombreTraductor = models.CharField(max_length=50)
    apellidoPaternoTraductor = models.CharField(max_length=50)
    apellidoMaternoTraductor = models.CharField(max_length=50)
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)