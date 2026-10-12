from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante

# AUTH
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 🔐 LOGIN
def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=correo)
            user = authenticate(request, username=user_obj.username, password=password)

            if user:
                login(request, user)
                return redirect('/inicio/')  # 👈 CAMBIO CLAVE
            else:
                return render(request, 'login.html', {
                    'error': 'Contraseña incorrecta'
                })

        except User.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Correo no registrado'
            })

    return render(request, 'login.html')


# 🚪 LOGOUT
def cerrar_sesion(request):
    logout(request)
    return redirect('/login/')


# 📝 REGISTRO
def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if User.objects.filter(email=correo).exists():
            return render(request, 'registro.html', {
                'error': 'El correo ya existe'
            })

        User.objects.create_user(
            username=correo,
            email=correo,
            password=password,
            first_name=nombre
        )

        return redirect('/login/')

    return render(request, 'registro.html')


# 🏠 INICIO (PÁGINA EVA)
@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'inicio.html')


# 📋 LISTA (PROTEGIDA)
@login_required(login_url='/login/')
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista.html', {'estudiantes': estudiantes})


# ➕ AGREGAR (PROTEGIDO)
@login_required(login_url='/login/')
def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        correo = request.POST.get('correo')

        Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            correo=correo
        )
        return redirect('/')

    return render(request, 'agregar.html')



@login_required(login_url='/login/')
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('/')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def modulo_arduino(request):
    return render(request, 'arduino.html')


@login_required(login_url='/login/')
def modulo_ph(request):
    return render(request, 'ph.html')


@login_required(login_url='/login/')
def modulo_temperatura(request):
    return render(request, 'temperatura.html')


@login_required(login_url='/login/')
def modulo_turbidez(request):
    return render(request, 'turbidez.html')


@login_required(login_url='/login/')
def modulo_evaluacion(request):
    return render(request, 'evaluacion.html')
