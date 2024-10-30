from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    Serial = models.CharField(max_length=100)
    Área = models.CharField(max_length=100)
    Responsable = models.CharField(max_length=100)
    