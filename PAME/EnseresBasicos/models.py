from django.db import models
from vigilancia.models import Extranjero

class EnseresBasicos(models.Model):
    estacionMigratoria = models.CharField(max_length=50)
    fechaEnseres = models.DateField()
    horaEnseres = models.DateTimeField()
    papelaHigienico = models.BooleanField()
    kitPersonal = models.BooleanField()
    panialDesechable = models.BooleanField()
    toallaSanitaria = models.BooleanField()
    colchoneta = models.BooleanField()
    mantaTermica = models,models.BooleanField()
    delExtranjero = models.ForeignKey(Extranjero, models.CASCADE)
 # Create your models here.
