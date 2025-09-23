from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()


class Direccion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=200)


    def __str__(self):
        return self.direccion