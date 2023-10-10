from django.db import models
from vigilancia.models import Estacion, Proceso

# Create your models here.
class EntidadDefensora(models.Model):
    nombreEntidad = models.CharField(max_length=50)
    nombreTitular = models.CharField(max_length=50)
    apellidoPaternoTitular = models.CharField(max_length=50)
    apellidoMaternoTitular = models.CharField(max_length=50)
    cargoTitular = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)

OPCION_ESTATUSATN_CHOICES=[
    ('Enviado','activo'),
    ('Aprobado','inactivo'),
]

class Defensoria(models.Model):
    delaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    delaEntidad = models.ForeignKey(EntidadDefensora, on_delete=models.CASCADE)
    delProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    fechaHora = models.DateTimeField()
    estatusAtencion = models.CharField(verbose_name='Estatus', max_length=25, choices=OPCION_ESTATUSATN_CHOICES, default='Enviado')

class ListadoPorAsignar(models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    delaDefensoria = models.ForeignKey(Defensoria, on_delete=models.CASCADE)

class Defensores(models.Model):
    nombreDefensor = models.CharField(max_length=50)
    apellidoPaternoDefensor = models.CharField(max_length=50)
    apellidoMaternoDefensor = models.CharField(max_length=50)
    cedulaDefensor = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    delaEntidad = models.ForeignKey(EntidadDefensora, on_delete=models.CASCADE)

class AsignaDefensor(models.Model):
    delaDefensoria = models.ForeignKey(Defensoria, on_delete=models.CASCADE)
    fechaHora = models.DateTimeField()
    oficio = models.FileField(upload_to='files/', verbose_name='Oficio', null=True, blank=True)
    delDefensor = models.ForeignKey(Defensores, on_delete=models.CASCADE)

class ListadoDefendidos(models.Model):
    delaAsignacion = models.ForeignKey(AsignaDefensor, on_delete=models.CASCADE)
    delProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

