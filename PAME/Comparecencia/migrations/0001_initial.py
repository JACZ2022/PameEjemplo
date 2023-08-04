# Generated by Django 4.2.3 on 2023-08-01 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vigilancia', '0002_alter_oficiopuestadisposicionac_numerooficio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VictimaDelito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacionAutoridad', models.TextField()),
                ('fechaNotificacion', models.DateField()),
                ('documentoMigratorio', models.BinaryField()),
                ('asunto', models.BinaryField()),
                ('documentoFGR', models.BinaryField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
        migrations.CreateModel(
            name='Refugio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacionComar', models.TextField()),
                ('fechaNotificacion', models.DateField()),
                ('contstanciaAdmisnion', models.BinaryField()),
                ('acuerdoSuspension', models.BinaryField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
        migrations.CreateModel(
            name='Consular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=50)),
                ('fechaNotificacionConsular', models.DateField()),
                ('horaNotificacionConsular', models.DateTimeField()),
                ('consulado', models.CharField(max_length=50)),
                ('tipoResolucion', models.CharField(max_length=50)),
                ('numeroOficio', models.CharField(max_length=50)),
                ('asunto', models.BinaryField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
        migrations.CreateModel(
            name='Comparecencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaComparecencia', models.DateField()),
                ('horaComparecencia', models.DateTimeField()),
                ('estadoCivil', models.CharField(max_length=50)),
                ('escolaridad', models.CharField(max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('lugarOrigen', models.CharField(max_length=50)),
                ('calleDomicilioPais', models.CharField(max_length=50)),
                ('numeroDomicilioPais', models.IntegerField()),
                ('localidadPais', models.CharField(max_length=50)),
                ('domicilioEnMexico', models.BooleanField()),
                ('nombrePadre', models.CharField(max_length=50)),
                ('apellidoPaternoPadre', models.CharField(max_length=50)),
                ('apellidoMaternoPadre', models.CharField(max_length=50)),
                ('nombreMadre', models.CharField(max_length=50)),
                ('apellidoPaternoMadre', models.CharField(max_length=50)),
                ('apellidoMaternoMadre', models.CharField(max_length=50)),
                ('designaRepresentanteLegal', models.BooleanField()),
                ('nombreRepresentante', models.CharField(max_length=50)),
                ('apellidoPaternoRepresentante', models.CharField(max_length=50)),
                ('apellidoMaternoRepresentante', models.CharField(max_length=50)),
                ('fechaIngresoMexico', models.DateField()),
                ('lugarIngresoMexico', models.CharField(max_length=50)),
                ('formaIngresoMexico', models.CharField(max_length=50)),
                ('decalaracion', models.TextField()),
                ('solicitaRefugio', models.BooleanField()),
                ('victimaDelito', models.BooleanField()),
                ('delExtranjero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vigilancia.extranjero')),
            ],
        ),
    ]
