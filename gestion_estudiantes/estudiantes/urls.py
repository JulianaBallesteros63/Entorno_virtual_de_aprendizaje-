

from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='login'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),

    path('inicio/', views.inicio, name='inicio'),
    path('panel/', views.panel_por_rol, name='panel_por_rol'),
    path('docente/', views.panel_docente, name='panel_docente'),
    path('administrador/', views.panel_administrador,
         name='panel_administrador'),

    path('arduino/', views.modulo_arduino, name='arduino'),
    path('ph/', views.modulo_ph, name='ph'),
    path('temperatura/', views.modulo_temperatura, name='temperatura'),
    path('turbidez/', views.modulo_turbidez, name='turbidez'),
    path('evaluacion/', views.modulo_evaluacion, name='evaluacion'),

    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante,
         name='eliminar_estudiante'),
]
