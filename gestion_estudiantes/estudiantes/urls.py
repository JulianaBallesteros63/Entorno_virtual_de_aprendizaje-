from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='login'),  # 👈 LOGIN como principal
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('inicio/', views.inicio, name='inicio'),

    path('lista/', views.lista_estudiantes, name='lista_estudiantes'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('logout/', views.cerrar_sesion, name='logout'),
]