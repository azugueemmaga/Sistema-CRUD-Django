from django.db import models

# Create your models here.

class Estudiante(models.Model):
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    anio = models.CharField(max_length=20)
    seccion = models.CharField(max_length=1)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Note 1
    nota2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Note 2
    nota3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Note 3
    promedio = models.DecimalField(max_digits=5, decimal_places=1,default=0)  # Average

    def calcular_promedio(self):
        if self.nota1 and self.nota2 and self.nota3:
            self.promedio = (self.nota1 + self.nota2 + self.nota3) / 3
            self.save()
    