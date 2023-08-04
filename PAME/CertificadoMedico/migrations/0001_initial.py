# Generated by Django 4.2.3 on 2023-08-03 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vigilancia', '0002_alter_oficiopuestadisposicionac_numerooficio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidadMigratoria', models.CharField(max_length=50)),
                ('fechaConsulta', models.DateField()),
                ('horaConsulta', models.DateTimeField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
        migrations.CreateModel(
            name='recetaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnidadMigratoria', models.CharField(max_length=50)),
                ('fechaReceta', models.DateField()),
                ('horaReceta', models.CharField(max_length=50)),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMedico', models.CharField(max_length=50)),
                ('apellidoPaternoMedico', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='PadecimientosActuales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diarrea', models.BooleanField()),
                ('infeccionesRespiratorias', models.BooleanField()),
                ('fiebre', models.BooleanField()),
                ('hemorragias', models.BooleanField()),
                ('nauseasVomito', models.BooleanField()),
                ('tos', models.BooleanField()),
                ('dolores', models.BooleanField()),
                ('lesionesPiel', models.BooleanField()),
                ('mareosVertigo', models.BooleanField()),
                ('tabaquismo', models.BooleanField()),
                ('bebidasAlcoholicas', models.BooleanField()),
                ('toxicomanias', models.TextField()),
                ('tipoDieta', models.CharField(max_length=50)),
                ('sintomasCovid', models.TextField()),
                ('embarazo', models.BooleanField()),
                ('tiempoEmbarazo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conclusiondiagnostica', models.TextField()),
                ('observaciones', models.TextField()),
                ('tratamiento', models.TextField()),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='ExploracionFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frecuenciaRespiratoria', models.IntegerField()),
                ('presionArterialSistolica', models.IntegerField()),
                ('presionArterialDiastolica', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estatura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oxigenacionSaturacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oxigenacionFrecuencia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indiceMasaCorporal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='certificadoMedicoEgreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnidadMigratoria', models.CharField(max_length=50)),
                ('fechaCertificadoEgerso', models.DateField()),
                ('horaCertificadoEgreso', models.CharField(max_length=50)),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='certificadoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnidadMigratoria', models.CharField(max_length=50)),
                ('fechaCertificado', models.DateField()),
                ('horaCertificado', models.CharField(max_length=50)),
                ('delaConsulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertificadoMedico.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hepatitis', models.BooleanField()),
                ('tubercolisis', models.BooleanField()),
                ('paludismo', models.BooleanField()),
                ('dengue', models.BooleanField()),
                ('colera', models.BooleanField()),
                ('hipertension', models.BooleanField()),
                ('cardiopatias', models.BooleanField()),
                ('vih', models.BooleanField()),
                ('otrosAntecedentes', models.TextField()),
                ('antecedentesQuirurgicos', models.TextField()),
                ('padecimientosCronicos', models.TextField()),
                ('alergias', models.TextField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
    ]
