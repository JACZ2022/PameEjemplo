from django.db import models


# Create your models here.


class EstacionMigratoria(models.Model):
    nombreEstacion = models.CharField(max_length=50)
        