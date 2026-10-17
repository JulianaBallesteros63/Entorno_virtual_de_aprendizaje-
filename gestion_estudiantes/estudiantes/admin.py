
from django.contrib import admin
from .models import Estudiante, Perfil


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'correo')
    search_fields = ('nombre', 'apellido', 'correo')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')
    list_filter = ('rol',)
    search_fields = ('usuario__username', 'usuario__email')
