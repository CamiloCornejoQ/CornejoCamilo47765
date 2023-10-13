from django import forms
from .models import Autor, Genero, Libro
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.views import PasswordChangeView

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento','nacionalidad']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre', 'descripcion',]

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor','genero','publicacion']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name= forms.CharField(label='Nombre',required=False)
    last_name= forms.CharField(label='Apellido',required=False)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 

class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CambiarContraseñaView(PasswordChangeView):
    success_url = reverse_lazy('Aplicacion/inicio.html')