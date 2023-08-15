from django.db import models
from vigilancia.models import Extranjero

class ExpedienteMedico(models.Model):
    ServicioMedicoExterno = models.CharField(max_length=100)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)


class Consulta(models.Model):
    unidadMigratoria = models.CharField(max_length=50)
    fechaConsulta = models.DateField()
    horaConsulta = models.DateTimeField()
    delExpedienteMedico = models.ForeignKey(ExpedienteMedico, on_delete=models.CASCADE)
    

class PerfilMedico(models.Model):
    nombreMedico = models.CharField(max_length=50)
    apellidoPaternoMedico = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
class ExploracionFisica(models.Model):
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    frecuenciaRespiratoria = models.IntegerField()
    presionArterialSistolica = models.IntegerField()
    presionArterialDiastolica =models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    estatura = models.DecimalField(max_digits=10, decimal_places=2)
    oxigenacionSaturacion = models.DecimalField(max_digits=10, decimal_places=2)
    oxigenacionFrecuencia = models.DecimalField(max_digits=10, decimal_places=2)
    indiceMasaCorporal = models.DecimalField(max_digits=10, decimal_places=2)
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
class Antecedentes(models.Model):
    hepatitis = models.BooleanField()
    tubercolisis = models.BooleanField()
    paludismo = models.BooleanField()
    dengue = models.BooleanField()
    colera = models.BooleanField()
    hipertension = models.BooleanField()
    cardiopatias = models.BooleanField()
    vih = models.BooleanField()
    otrosAntecedentes = models.TextField()
    antecedentesQuirurgicos = models.TextField()
    padecimientosCronicos= models.TextField()
    alergias = models.TextField()
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    
class PadecimientosActuales(models.Model):
    diarrea = models.BooleanField()
    infeccionesRespiratorias =models.BooleanField()
    fiebre=models.BooleanField()
    hemorragias = models.BooleanField()
    nauseasVomito= models.BooleanField()
    tos = models.BooleanField()
    dolores=models.BooleanField()
    lesionesPiel = models.BooleanField()
    mareosVertigo=models.BooleanField()
    tabaquismo=models.BooleanField()
    bebidasAlcoholicas = models.BooleanField()
    toxicomanias = models.TextField()
    tipoDieta = models.CharField(max_length=50)
    sintomasCovid=models.TextField()
    embarazo = models.BooleanField()
    tiempoEmbarazo=models.DecimalField(max_digits=10, decimal_places=2)
    conclusiondiagnostica= models.TextField()
    observaciones =models.TextField()
    tratamiento = models.TextField()
    delaConsulta = models.ForeignKey(Consulta, on_delete= models.CASCADE)
    
class CertificadoMedico(models.Model):
    UnidadMigratoria = models.CharField(max_length=50)
    fechaCertificado = models.DateField()
    horaCertificado = models.CharField(max_length=50)
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
class RecetaMedica(models.Model):
    diagnostico = models.TextField()
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

class detalleTratmiento(models.Model):
    dosis = models.IntegerField()
    unidad = models.CharField(max_length=50)
    nombreMedicamento = models.CharField(max_length=50)
    descipcion = models.CharField(max_length=100)
    delaReceta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE)


class CertificadoMedicoEgreso(models.Model):
    UnidadMigratoria = models.CharField(max_length=50)
    fechaCertificadoEgreso = models.DateField()
    horaCertificadoEgreso= models.CharField(max_length=50)
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
class ReferenciaMedica(models.Model):
    diagnostico = models.TextField()
    unidadMedica = models.TextField()
    documentoAtencionExterna = models.CharField(max_length=100)
    delaConsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
# Create your models here.
