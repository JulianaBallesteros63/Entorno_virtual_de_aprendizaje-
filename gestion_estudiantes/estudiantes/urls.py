from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
]