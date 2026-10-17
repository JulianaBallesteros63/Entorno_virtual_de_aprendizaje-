
from django.db import models
from django.contrib.auth.models import User


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    ROLES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('administrador', 'Administrador'),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='estudiante'
    )

    def __str__(self):
        return f'{self.usuario.username} - {self.rol}'
