from django.db import models
from vigilancia.models import Extranjero


class Notificcion(models.Model):
    consulado = models.CharField(max_length=50)
    tipoResolucion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    fechaNotificacion = models.DateField()
    horaNotificacion = models.DateTimeField()
    asunto = models.TextField()
    documentacion = models.CharField(max_length=100)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
# Create your models here.
