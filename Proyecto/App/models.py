from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

def __str__(self):
    return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=140, default='Descripcion')

def __str__(self):
    return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    publicacion = models.DateField()

def __str__(self):
    return self.titulo
