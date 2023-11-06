from django.db import models
from vigilancia.models import Proceso, Estacion, Extranjero
from comparecencia.models import Comparecencia
from catalogos.models import AutoridadActuante, Consulado, Fiscalia
# Create your models here.


class Notificacion(models.Model):
    fechaAceptacion = models.DateField(verbose_name='Fecha de Aceptación', auto_now_add=True)
    no_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name='Número de Proceso Asociado', related_name='notificaciones_juridico')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, verbose_name='Estación de Notificación')
    
    # Campos adicionales que podrías necesitar en el futuro...
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    estatus_notificacion = models.CharField(max_length=50, verbose_name='Estatus de Notificación', blank=True, null=True)

    def __str__(self):
        return f"Notificación de {self.no_proceso.extranjero.nombreExtranjero} en {self.estacion.nombre}"

ACCION= (
    ('Deportacion', 'DEPORTACION'),
    ('Retorno_Asistido', 'RETORNO ASISTIDO'),
)

class NotificcionConsular(models.Model):
    delaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fechaNotificacion= models.DateField()
    horaNotificacion = models.DateTimeField()
    numeroOficio = models.CharField(max_length=50)
    delConsulado = models.ForeignKey(Consulado, on_delete=models.CASCADE)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    accion = models.CharField(max_length=50, choices= ACCION)
    delaAutoridad = models.ForeignKey(AutoridadActuante, on_delete=models.CASCADE)

class NotificacionCOMAR(models.Model):
    delaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fechaNotificacion= models.DateField()
    numeroOficio = models.CharField(max_length=50)
    delExtranjero= models.ForeignKey(Extranjero, on_delete=models.CASCADE)
    #Datos COMAR
    notificacionComar= models.TextField()
    delProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    delaComparecencia = models.ForeignKey(Comparecencia, on_delete=models.CASCADE)
    delaAutoridad = models.ForeignKey(AutoridadActuante, on_delete=models.CASCADE)
    contstanciaAdmision_Rechazo = models.FileField(verbose_name="Constancia de Admisión/Rechazo:",upload_to='files/', null=True, blank=True)
    acuerdoSuspension = models.FileField(verbose_name="Acuerdo Suspensión:",upload_to='files/', null=True, blank=True)

CONDCION = (
    ('Victima', 'VICTIMA'),
    ('Testigo', 'TESTIGO'),
)

class NotificacionFiscalia(models.Model):
    delaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fechaNotificacion= models.DateField()
    horaNotificacion = models.DateTimeField()
    numeroOficio = models.CharField(max_length=50)
    delaFiscalia = models.ForeignKey(Fiscalia, on_delete=models.CASCADE)
    delaComparecencia = models.ForeignKey(Comparecencia, on_delete=models.CASCADE)
    condicion = models.CharField(max_length=50, choices= CONDCION)
    documentoFGR = models.CharField(max_length=100)


