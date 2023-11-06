from django.db import models


# Create your models here.
class Tipos(models.Model):
    tipo = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Tipos"
    
class Estatus(models.Model):
    tipoEstatus = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.tipoEstatus
    
    class Meta:
        verbose_name_plural = "Estatus"
    
class Estado(models.Model):
    estado = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.estado
    
class Fiscalia(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=100, null=False)
    correoElectronico = models.CharField(max_length=100, null=False)
    delEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Consulado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=100, null=False)
    correoElectronico = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.nombre
    
class Responsable(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidoPat = models.CharField(max_length=50, null=False)
    apellidoMat = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False)
    telefono = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        return self.nombre
    
class AutoridadActuante(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidoPat = models.CharField(max_length=50, null=False)
    apellidoMat = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False)
    telefono = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        return self.nombre
    


class OficinaRepresentacion(models.Model):
    identificador = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    delEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)

OPCION_CLASE_CHOICES=[
    ('ESTACION','estacion'),
    ('ESTANCIA','estancia'),
]

class Estacion(models.Model):
    identificador = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    calle = models.CharField(max_length=50, null=False)
    noext = models.CharField(max_length=5)
    noint = models.CharField(max_length=5, default='sn')
    colonia = models.CharField(max_length=50, null=False)
    cp = models.IntegerField(null=False)
    poblacion = models.CharField(max_length=50, null= False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)
    clase = models.CharField(verbose_name='Clase estacion', max_length= 20, choices = OPCION_CLASE_CHOICES, default='Estacion')
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE)
    capacidad = models.IntegerField( null=False)
    delaOficina = models.ForeignKey(OficinaRepresentacion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Estaciones"
class Salida(models.Model):
    tipoSalida = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.tipoSalida
    
class Estancia(models.Model):
    tipoEstancia = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.tipoEstancia
    
class Relacion(models.Model):
    tipoRelacion = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.tipoRelacion
