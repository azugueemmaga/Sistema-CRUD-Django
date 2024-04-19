from django.db import models

# Create your models here.

class Estudiante(models.Model):
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)