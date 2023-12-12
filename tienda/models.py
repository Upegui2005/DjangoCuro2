from django.db import models

# Create your models here.

class Productos(models.Model):
    COLECCIONES = (
        (1, 'Curandera'),
    ) 
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    coleccion = models.IntegerField(choices=COLECCIONES, default=1)
    foto = models.ImageField(null=True, blank=True, default='fotos_productos/default.png', upload_to='fotos_productos')

class Usuarios(models.Model):
    ROLES = (
        (1, 'Administrador'),
        (2, 'Usuario'),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=16)
    rol = models.IntegerField(choices=ROLES, default=2)