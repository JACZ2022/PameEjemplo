from django.db import models
from vigilancia.models import Extranjero
from catalogos.models import Estacion, Responsable

# Create your models here.
class TipoAcuerdo(models.Model):
    tipo = models.CharField()

class Acuerdo(models.Model):
    delAcuerdo = models.ForeignKey(TipoAcuerdo, on_delete=models.CASCADE)
    fechaAcuerdo = models.DateField()
    numeroExpediente = models.CharField(max_length=50)
    horaAcuerdo = models.TimeField()
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    delResponsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    nombreTestigoUno = models.CharField(max_length=50)
    apellidoPaternoTestigoUno = models.CharField(max_length=50)
    apellidoMaternoTestigoUno = models.CharField(max_length=50)
    firmaTestigoUno = models.BinaryField()
    huellaTestigoUno = models.BinaryField()
    nombreTestigoDos = models.CharField(max_length=50)
    apellidoPaternoTestigoDos = models.CharField(max_length=50)
    apellidoMaternoTestigoDos = models.CharField(max_length=50)
    firmaTestigoDos = models.BinaryField()
    huellaTestigoDos = models.BinaryField()
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    nombreTraductor = models.CharField(max_length=50)
    apellidoPaternoTraductor = models.CharField(max_length=50)
    apellidoMaternoTraductor = models.CharField(max_length=50)
    razonContinuidad_Continuacion = models.TextField(null=True, blank = True)
    fechaSuspensión_Continuacion = models.DateField(null=True, blank=True)
    autoridadEmisora_Acumulacion = models.TextField(null=True, blank = True)
    numeroExpedienteAnterior_Acumulacion =models.CharField(max_length=50, null=True, blank =True)
    antecedentes_conclusion = models.TextField(null=True, blank = True)
    delegatorio_inicio = models.TextField(null=True, blank = True)
    descripcion_recepcion = models.TextField(null=True, blank = True)
    fundamento_separacion = models.TextField(null=True, blank = True)
    razon_suspension = models.TextField(null=True, blank = True)
    declaracionExtanjero_comparecencia = models.TextField(null=True, blank = True)
    estacionDestino_traslado = models.CharField(max_length=50, null=True, blank = True)
    motivo_traslado = models.TextField(null=True, blank = True)
    documentoAcuerdo= models.FileField(upload_to='files/', null=True, blank=True)


