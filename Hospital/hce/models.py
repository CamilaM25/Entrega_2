from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.TextField(max_length=60)
    Marca = models.TextField(max_length=60)
    Modelo = models.TextField(max_length=60)
    Serial = models.TextField(max_length=60)
    Area = models.TextField(max_length=60, default='Default Area')
    Responsable = models.IntegerField()
    

class Responsable(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.TextField(max_length=30)
    nombre = models.TextField(max_length=60)
    apellido = models.TextField(max_length=60)
    correo = models.TextField(max_length=100)
