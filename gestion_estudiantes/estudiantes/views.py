from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante

# AUTH
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 🔐 LOGIN con correo
def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=correo)
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Correo no registrado'})

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
                'error': 'El correo ya está registrado'
            })

        user = User.objects.create_user(
            username=correo,   # usamos correo como username
            email=correo,
            password=password,
            first_name=nombre
        )

        login(request, user)
        return redirect('/')

    return render(request, 'registro.html')


# 📋 LISTA (protegida)
@login_required(login_url='/login/')
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista.html', {'estudiantes': estudiantes})


# ➕ AGREGAR
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


# ❌ ELIMINAR
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('/')