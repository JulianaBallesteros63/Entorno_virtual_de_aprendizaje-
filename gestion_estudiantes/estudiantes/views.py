
from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Estudiante, Perfil


def rol_requerido(*roles):
    def decorador(vista):
        @wraps(vista)
        def envoltura(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            perfil, creado = Perfil.objects.get_or_create(
                usuario=request.user,
                defaults={'rol': 'estudiante'}
            )

            if perfil.rol not in roles:
                return redirect('panel_por_rol')

            return vista(request, *args, **kwargs)

        return envoltura
    return decorador


# INICIO DE SESION
def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo', '').strip()
        password = request.POST.get('password', '')

        try:
            user_obj = User.objects.get(email__iexact=correo)
        except User.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Correo no registrado'
            })

        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('panel_por_rol')

        return render(request, 'login.html', {
            'error': 'Contraseña incorrecta'
        })

    return render(request, 'login.html')


# CERRAR SESION
@login_required(login_url='/login/')
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


# REGISTRO DE ESTUDIANTES
def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        password = request.POST.get('password', '')

        if not nombre or not correo or not password:
            return render(request, 'registro.html', {
                'error': 'Todos los campos son obligatorios'
            })

        if User.objects.filter(email__iexact=correo).exists():
            return render(request, 'registro.html', {
                'error': 'El correo ya existe'
            })

        usuario = User.objects.create_user(
            username=correo,
            email=correo,
            password=password,
            first_name=nombre
        )

        Perfil.objects.create(
            usuario=usuario,
            rol='estudiante'
        )

        return redirect('login')

    return render(request, 'registro.html')


# REDIRECCION SEGUN EL ROL
@login_required(login_url='/login/')
def panel_por_rol(request):
    perfil, creado = Perfil.objects.get_or_create(
        usuario=request.user,
        defaults={'rol': 'estudiante'}
    )

    if perfil.rol == 'docente':
        return redirect('panel_docente')

    if perfil.rol == 'administrador':
        return redirect('panel_administrador')

    return redirect('inicio')


# PANEL DEL ESTUDIANTE
@rol_requerido('estudiante')
def inicio(request):
    return render(request, 'inicio.html')


# PANEL DEL DOCENTE
@rol_requerido('docente')
def panel_docente(request):
    return render(request, 'docente.html')


# PANEL DEL ADMINISTRADOR
@rol_requerido('administrador')
def panel_administrador(request):
    return render(request, 'administrador.html')


# LISTA DE ESTUDIANTES
@rol_requerido('administrador')
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista.html', {
        'estudiantes': estudiantes
    })


# AGREGAR ESTUDIANTE
@rol_requerido('administrador')
def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        edad = request.POST.get('edad', '').strip()
        correo = request.POST.get('correo', '').strip()

        if not nombre or not apellido or not edad or not correo:
            return render(request, 'agregar.html', {
                'error': 'Todos los campos son obligatorios'
            })

        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
        except ValueError:
            return render(request, 'agregar.html', {
                'error': 'La edad debe ser un número válido'
            })

        Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            correo=correo
        )

        return redirect('lista_estudiantes')

    return render(request, 'agregar.html')


# ELIMINAR ESTUDIANTE
@rol_requerido('administrador')
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')

    return redirect('lista_estudiantes')


# MODULOS EDUCATIVOS
@rol_requerido('estudiante')
def modulo_arduino(request):
    return render(request, 'arduino.html')


@rol_requerido('estudiante')
def modulo_ph(request):
    return render(request, 'ph.html')


@rol_requerido('estudiante')
def modulo_temperatura(request):
    return render(request, 'temperatura.html')


@rol_requerido('estudiante')
def modulo_turbidez(request):
    return render(request, 'turbidez.html')


@rol_requerido('estudiante')
def modulo_evaluacion(request):
    return render(request, 'evaluacion.html')
