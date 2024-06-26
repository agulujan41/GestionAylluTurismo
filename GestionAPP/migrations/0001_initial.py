# Generated by Django 4.2.7 on 2024-05-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('precio', models.FloatField()),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
