# Generated by Django 4.2.7 on 2024-05-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugares',
            name='picture',
            field=models.ImageField(upload_to='./GestionAPP/lugares_images'),
        ),
    ]