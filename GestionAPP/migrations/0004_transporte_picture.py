# Generated by Django 4.2.7 on 2024-05-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAPP', '0003_transporte_excursiones'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporte',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='./GestionAPP/transporte_images'),
        ),
    ]
