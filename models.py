from django.db import models

# Create your models here.
from django.db import models
from vigilancia.models import Extranjero, Proceso
from catalogos.models import Estacion



    

class PerfilMedico(models.Model):
    nombreMedico = models.CharField(max_length=50)
    apellidoPaternoMedico = models.CharField(max_length=50)
    apellidoMaternoMedico = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)


class Consulta(models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete= models.CASCADE)
    delaEstacion = models.ForeignKey(Estacion, on_delete= models.CASCADE)
    delMedico = models.ForeignKey(PerfilMedico, on_delete=models.CASCADE)
    fechaConsulta = models.DateField()
    horaConsulta = models.DateTimeField()
# Exploracion física
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    frecuenciaRespiratoria = models.IntegerField()
    presionArterialSistolica = models.IntegerField()
    presionArterialDiastolica =models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    estatura = models.DecimalField(max_digits=10, decimal_places=2)
    oxigenacionSaturacion = models.DecimalField(max_digits=10, decimal_places=2)
    oxigenacionFrecuencia = models.DecimalField(max_digits=10, decimal_places=2)
    indiceMasaCorporal = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class ConsultaExterna(models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete= models.CASCADE)
    delaEstacion = models.ForeignKey(Estacion, on_delete= models.CASCADE)
    delMedico = models.ForeignKey(PerfilMedico, on_delete=models.CASCADE)
    fechaCconsulta = models.DateField()
    horaConsulta = models.CharField(max_length=50)
    diagnostico = models.TextField()
    unidadMedica = models.TextField()
    documentoAtencionExterna = models.FileField(verbose_name="Consulta externa",upload_to='files/', null=True, blank=True)
    
class RecetaMedica(models.Model):
    diagnostico = models.TextField()
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null = True, blank= True)
    delaConsultaExterna = models.ForeignKey(ConsultaExterna, on_delete=models.CASCADE, null = True, blank= True)
 
class detalleTratmiento(models.Model):
    dosis = models.IntegerField()
    unidad = models.CharField(max_length=50)
    nombreMedicamento = models.CharField(max_length=50)
    descipcion = models.CharField(max_length=100)
    delaReceta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE)


    

    
# Create your models here.