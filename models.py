
from django.db import models
from catalogos.models import Estacion
from vigilancia.models import Extranjero, Proceso
from consultaMedica.models import PerfilMedico

# Create your models here.

OPCION_TIPO_CHOICES= [
    [0,'INGRESO'],
    [1,'EGRESO'],
]
class CertificadoMedico(models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete= models.CASCADE)
    delaEstacion = models.ForeignKey(Estacion, on_delete= models.CASCADE)
    delMedico = models.ForeignKey(PerfilMedico, on_delete=models.CASCADE)
    fechaCertificado = models.DateField()
    horaCertificado = models.CharField(max_length=50)
    tipoCertificado = models.CharField(verbose_name='Tipo Certificado', max_length=25, choices=OPCION_TIPO_CHOICES, default='INGRESO')
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
# Antecedentes
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
#   Padecimientos actuales
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
    
class certificadoExterno(models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete= models.CASCADE)
    delaEstacion = models.ForeignKey(Estacion, on_delete= models.CASCADE)
    delMedico = models.ForeignKey(PerfilMedico, on_delete=models.CASCADE)
    fechaCertificado = models.DateField()
    horaCertificado = models.CharField(max_length=50)
    diagnostico = models.TextField()
    unidadMedica = models.TextField()
    documentoAtencionExterna = models.FileField(verbose_name="Certificado Externo:",upload_to='files/', null=True, blank=True)
    