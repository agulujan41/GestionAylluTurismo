# Generated by Django 4.2.7 on 2024-05-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAPP', '0005_transporte_anio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('DNI_pasaporte', models.CharField(max_length=50)),
            ],
        ),
    ]
