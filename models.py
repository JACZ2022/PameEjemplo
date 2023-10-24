from django.db import models
from vigilancia.models import Proceso, Extranjero
from catalogos.models import Estacion, Responsable

# Create your models here.

class ClasificaDoc(models.Model):
    clasificacion = models.CharField(max_length=50)


class TiposDoc (models.Model):
    descripcion = models.CharField(max_length=50)
    delaClasificacion = models.ForeignKey(ClasificaDoc, on_delete=models.CASCADE)

class repositorio (models.Model):
    delProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    fechaGeneracion = models.DateTimeField()
    delTipo = models.ForeignKey(TiposDoc, on_delete=models.CASCADE)
    delaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    delResponsable = models.ForeignKey(Responsable, models.CASCADE)
    archivo = models.FileField(verbose_name="Documento:",upload_to='files/', null=True, blank=True)


   
