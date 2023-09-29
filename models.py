from tabnanny import verbose
from django.db import models
from catalogos.models import Estacion, Responsable, Salida, Estancia, Relacion 
from PIL import Image, ExifTags

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=200,verbose_name='Nacionalidad')
    Abreviatura = models.CharField(max_length=200,verbose_name='Abreviatura')
    
    class Meta:
        verbose_name_plural = "Países"
    
    def __str__(self):
        return self.nombre

class PuestaDisposicionINM(models.Model):
    identificadorProceso = models.CharField(verbose_name='Número de Proceso', max_length=50)
    numeroOficio = models.CharField(verbose_name='Número de Oficio', max_length=50)
    fechaOficio = models.DateField(verbose_name='Fecha de Oficio')
    nombreAutoridadSignaUno = models.CharField(verbose_name='Nombre de Autoridad que firma (1)', max_length=100)
    cargoAutoridadSignaUno = models.CharField(verbose_name='Cargo de Autoridad que firma (1)', max_length=100)
    nombreAutoridadSignaDos = models.CharField(verbose_name='Nombre de Autoridad que firma (2)', max_length=100)
    cargoAutoridadSignaDos = models.CharField(verbose_name='Cargo de Autoridad que firma (2)', max_length=100)
    oficioPuesta = models.FileField(upload_to='files/', verbose_name='Oficio de Puesta', null=True, blank=True)
    oficioComision = models.FileField(upload_to='files/', verbose_name='Oficio de Comisión', null=True, blank=True)
    puntoRevision = models.CharField(verbose_name='Punto de Revisión', max_length=100)
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, verbose_name='Estación de Origen', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Puestas a Disposición INM"

    def __str__(self):
        return self.numeroOficio
    
    @property
    def extranjeros(self):
        return self.extranjeros.all()
    
OPCION_TIPODEP_CHOICES=[
    ('Estatal','estatal'),
    ('FEDERAL','federal'),
]

class Dependencias(models.Model):
    nombreDependencia = models.CharField(max_length=100)
    tipoDependencia = models.CharField(verbose_name='Tipo dependencia', max_length= 20, choices = OPCION_TIPODEP_CHOICES, default='Estatal')


class PuestaDisposicionAC(models.Model):
    identificadorProceso = models.CharField(verbose_name='Número de Proceso', max_length=50)
    numeroOficio = models.CharField(verbose_name='Número de Oficio', max_length=50)
    fechaOficio = models.DateField(verbose_name='Fecha de Oficio')
    nombreAutoridadSignaUno = models.CharField(verbose_name='Nombre de Autoridad que firma (1)', max_length=100)
    cargoAutoridadSignaUno = models.CharField(verbose_name='Cargo de Autoridad que firma (1)', max_length=100)
    nombreAutoridadSignaDos = models.CharField(verbose_name='Nombre de Autoridad que firma (2)', max_length=100)
    cargoAutoridadSignaDos = models.CharField(verbose_name='Cargo de Autoridad que firma (2)', max_length=100)
    oficioPuesta = models.FileField(upload_to='files/', verbose_name='Oficio de Puesta', null=True, blank=True)
    oficioComision = models.FileField(upload_to='files/', verbose_name='Oficio de Comisión', null=True, blank=True)
    puntoRevision = models.CharField(verbose_name='Punto de Revisión', max_length=100)
    dependencia = models.ForeignKey(Dependencias, on_delete= models.CASCADE, verbose_name='Dependencia')
    numeroCarpeta = models.CharField(verbose_name='Número de Carpeta', max_length=50)
    entidadFederativa = models.CharField(verbose_name='Entidad Federativa', max_length=100)
    municipio =models.CharField(max_length=50)
    certificadoMedico = models.FileField(upload_to='files/', verbose_name='Certificado Médico', null=True, blank=True)
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, verbose_name='Estación de Origen', null=True, blank=True)
    class Meta:
        verbose_name_plural = "Puestas a Disposicion AC"
    
    def __str__(self):
        return str(self.numeroOficio)
    
class PuestaDisposicionVP(models.Model):
    numeroOficio = models.CharField(max_length=50, verbose_name='Numero de Oficio')
    fechaOficio = models.DateField(verbose_name='Fecha de Oficio')
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, verbose_name="Estación de origen", null=True, blank=True)
    class Meta:
        verbose_name_plural = "Puestas a Disposición VP"
    def __str__(self):
        return str(self.numeroOficio) 


OPCION_GENERO_CHOICES=[
    [0,'HOMBRE'],
    [1,'MUJER'],
    [2, 'NO BINARIO']
]
OPCION_ESTATUS_CHOICES=[
    ('Activo','activo'),
    ('Inactivo','inactivo'),
]
class Extranjero(models.Model):
    fechaRegistro = models.DateField(verbose_name='Fecha de Registro', auto_now_add=True)
    horaRegistro = models.DateTimeField(verbose_name='Hora de Registro', auto_now_add=True)
    numeroExtranjero = models.CharField(verbose_name='Número de Extranjero', max_length=25, unique=True)
    deLaEstacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, verbose_name='Estación de Origen', null=True, blank=True)
    nombreExtranjero = models.CharField(verbose_name='Nombre de Extranjero', max_length=50, blank=True)
    apellidoPaternoExtranjero = models.CharField(verbose_name='Apellido Paterno de Extranjero', max_length=50, blank=True)
    apellidoMaternoExtranjero = models.CharField(verbose_name='Apellido Materno', max_length=50, blank=True, null=True, default=" ")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, verbose_name='País')
    genero = models.IntegerField(verbose_name='Género', choices=OPCION_GENERO_CHOICES)
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    documentoIdentidad = models.FileField(upload_to='files/', verbose_name='Documento de Identidad', null=True, blank=True)
    tipoEstancia = models.ForeignKey(Estancia, on_delete=models.CASCADE, verbose_name='Modalidad de Ingreso')
    estatus = models.CharField(verbose_name='Estatus', max_length=25, choices=OPCION_ESTATUS_CHOICES, default='Activo')
    viajaSolo = models.BooleanField(verbose_name='Viaja Solo', default=True)
    deLaPuestaIMN = models.ForeignKey(PuestaDisposicionINM, on_delete=models.CASCADE, blank=True, null=True, related_name='extranjeros', verbose_name='Puesta IMN')
    deLaPuestaAC = models.ForeignKey(PuestaDisposicionAC, on_delete=models.CASCADE, blank=True, null=True, related_name='extranjeros', verbose_name='Puesta AC')
    deLaPuestaVP = models.ForeignKey(PuestaDisposicionVP, on_delete=models.CASCADE, blank=True, null=True, related_name='extranjeros', verbose_name='Puesta VP')


    class Meta:
        verbose_name_plural = "Extranjeros" 
    def __str__(self):
         return self.nombreExtranjero
    
    def delete(self, *args, **kwargs):
        # Incrementar la capacidad de la estación al eliminar
        if self.deLaEstacion:
            self.deLaEstacion.capacidad += 1
            self.deLaEstacion.save()
        super().delete(*args, **kwargs)
    
class descripcion(models.Model):
    delExtranjero = models.OneToOneField(
        Extranjero, on_delete=models.CASCADE,
        primary_key=True,
    )
    estatura = models.DecimalField(max_digits=5, decimal_places=2)
    cejas = models.CharField(max_length=50)
    nariz = models.CharField(max_length=50)
    labios = models.CharField(max_length=50)
    tipoCabello = models.CharField(max_length=50)
    bigote = models.CharField(max_length=50)
    complexion = models.CharField(max_length=50)
    frente = models.CharField(max_length=50)
    colorOjos=models.CharField(max_length=50)
    boca = models.CharField(max_length=50)
    segnasParticulares = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)   

class Acompanante(models.Model):
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE, blank=True, null=True, related_name='acompanantes_delExtranjero')
    delAcompanante = models.ForeignKey(Extranjero, on_delete=models.CASCADE, blank=True, null=True, related_name='acompanantes_delAcompanante')
    relacion = models.ForeignKey(Relacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.delExtranjero} - {self.delAcompanante}"

    class Meta:
        verbose_name_plural = "Acompañantes"


class Biometrico(models.Model):
    Extranjero = models.OneToOneField(
        Extranjero, on_delete=models.CASCADE,
        primary_key=True,
    )
    fotografiaExtranjero = models.FileField(verbose_name="Fotografía del Extranjero:", upload_to='files/', null=True, blank=True)
    fechaHoraFotoCreate = models.DateTimeField(auto_now_add=True)
    fechaHoraFotoUpdate = models.DateTimeField(auto_now_add=True)
    huellaExtranjero = models.FileField(verbose_name="Huella del Extranjero:",upload_to='files/', null=True, blank=True)
    fechaHoraHuellaCreate = models.DateTimeField(auto_now_add=True)
    fechaHoraHuellaUpdate = models.DateTimeField(auto_now_add=True)

    firmaExtranjero = models.FileField(verbose_name="Firma del Extranjero:",upload_to='files/', null=True, blank=True)
    fechaHoraFirmaCreate = models.DateTimeField(auto_now_add=True)
    fechaHoraFirmaUpdate = models.DateTimeField(auto_now_add=True)
    

        

    class Meta:
        verbose_name_plural = 'Biometricos'
        
class Proceso(models.Model):
    agno = models.IntegerField()
    estacionInicio = models.CharField(max_length=50)
    estacionFinal = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    numeroUnicoProceso = models.IntegerField()
    carpeta = models.CharField(max_length=100)
    delExtranjero = models.ForeignKey(Extranjero, on_delete=models.CASCADE)
  
 