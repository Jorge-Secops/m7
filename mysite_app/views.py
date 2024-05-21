from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, InmuebleForm
from .models import Inmueble

#login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#registro
def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

#perfil
def perfil_view(request):
    return render(request, 'perfil.html')

#logout
def logout_view(request):
    logout(request)
    return redirect('login')

#editar perfil
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

#agregar vivienda
@login_required
def agregar_vivienda(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = InmuebleForm()
    return render(request, 'agregar_vivienda.html', {'form': form})

#inicio
def index(request):
    return render(request, 'index.html')

#editar inmueble
'''def editar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inicio')  
    else:
        form = InmuebleForm(instance=inmueble)
    
    return render(request, 'editar_inmueble.html', {'form': form})'''#esta se usara una vez creada la base de datos

def editar_inmueble(request):
    form = InmuebleForm()  # Crear un formulario vacío

    return render(request, 'editar_inmueble.html', {'form': form})

#ofeertas
def ver_oferta(request):
    
    viviendas = Inmueble.objects.all()
    return render(request, 'ver_oferta.html', {'viviendas': viviendas})