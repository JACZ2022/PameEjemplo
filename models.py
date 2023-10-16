from django.db import models
from vigilancia.models import Extranjero
from catalogos.models import Estacion, Responsable, AutoridadActuante

# Create your models here.
class TipoResolucion(models.Model):
    tipoResolutivo = models.CharField(max_length=50)

class Resolucion(models.Model):
    delaResolucion = models.ForeignKey(TipoResolucion, on_delete=models.CASCADE)
    fecharesolucion = models.DateField()
    numeroExpediente = models.CharField(max_length=50)
    horaResolucion = models.TimeField()
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)
    delResponsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    delExtanjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    fechaNacimiento_DocumentoProvisional = models.DateField()
    vinculoFamiliar = models.CharField(max_length=50)
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
    nombreTraductor = models.CharField(max_length=50)
    apellidoPaternoTraductor = models.CharField(max_length=50)
    apellidoMaternoTraductor = models.CharField(max_length=50)
    cargoTraductor = models.CharField(max_length=50)
    breveDescripcion = models.TextField(null=True, blank = True)
    alegatos = models.TextField(null=True, blank = True)
    delaAutoridad = models.ForeignKey(AutoridadActuante, on_delete=models.CASCADE) 
    numeroOficioDefensoria_COMAR =models.CharField(max_length=50, null=True, blank =True)
    numeroOficioJuzgado_COMAR =models.CharField(max_length=50, null=True, blank =True)
    nombreAutoridadJuzgado_COMAR= models.TextField(null=True, blank = True)
    primerSupuesto_LibreTransito = models.TextField(null=True, blank = True)
    segundoSupuesto_LibreTransito = models.TextField(null=True, blank = True)
    fraccionAdecuada = models.TextField(null=True, blank = True)
    comparecencia_Art133 = models.TextField(null=True, blank = True)
    agnosRestriccion_Provicional = models.IntegerField()
    tipoDocumento_Provicional = models.CharField(max_length=50)
    numeroDocumento_Provicional = models.CharField(max_length=50)
    documentoAcuerdo= models.FileField(upload_to='files/', null=True, blank=True)