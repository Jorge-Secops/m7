from django import forms
from django.contrib.auth.models import User
from .models import Inmueble

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['titulo', 'descripcion', 'precio', 'ubicacion']

#el usuario podra editar l oque aparece en fields
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  
