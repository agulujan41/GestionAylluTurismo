from django.db import models

# Create your models here.
class Lugares(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300,blank=True,null=True,verbose_name="Descripción")
    ubicacionGEO = models.CharField(max_length=200,null=True,blank=True)
    picture = models.ImageField(upload_to="./GestionAPP/lugares_images")
    def __str__(self) :
        return f"{self.nombre.capitalize()}" 

class Transporte(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(null=True,blank=True)
    patente = models.CharField(max_length=10)
    nombre_propietario = models.CharField(max_length=50,null=True,blank=True)
    apellido_propietario = models.CharField(max_length=50,null=True,blank=True)
    empresa_propietario = models.CharField(max_length=50,null=True,blank=True)
    cuit_propietario = models.CharField(max_length=50,null=True,blank=True)
    picture = models.ImageField(upload_to="./GestionAPP/transporte_images",null=True,blank=True)
    def __str__(self) :
        return f"{self.marca.capitalize()} - {self.modelo.capitalize()} - {self.apellido_propietario}, {self.nombre_propietario} "
class Excursiones(models.Model):
    lugar = models.ForeignKey(Lugares,on_delete=models.CASCADE)
    anotacion = models.CharField(max_length=100)
    precio = models.FloatField()
    def __str__(self) :
        return f"{self.lugar.capitalize()} - {self.precio}" 
class Viaje(models.Model):
    excursion = models.ForeignKey(Excursiones,on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField()
    fecha_retorno = models.DateTimeField()
    transporte = models.ForeignKey(Transporte,on_delete=models.CASCADE,null=True,blank=True)

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DNI_pasaporte = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.apellido}, {self.nombre} - {self.DNI_pasaporte}"

class Voucher(models.Model):
    fecha_emision = models.DateTimeField()
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)

class Voucher_con_Excursion():
    voucher = models.ForeignKey(Voucher,on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursiones,on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad = models.IntegerField()

