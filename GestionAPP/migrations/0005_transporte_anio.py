# Generated by Django 4.2.7 on 2024-05-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAPP', '0004_transporte_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporte',
            name='anio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]