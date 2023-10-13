from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Genero, Libro
from .forms import AutorForm, GeneroForm, LibroForm
from .forms import *
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render






def inicio(request):
    return render(request,'Aplicacion/inicio.html')

def about(request):
    return render(request,'Aplicacion/about.html')

# Vista para crear un autor
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Aplicacion/inicio.html')
    else:
        form = AutorForm()
    return render(request, 'Aplicacion/autor_crear.html', {'form': form})

# Vista para ver la lista de autores
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'Aplicacion/autores_lista.html', {'autores': autores})

# Vista para editar un autor
def editar_autor(request, nombre_autor):
    try:
        autor = Autor.objects.get(nombre=nombre_autor)
    except Autor.DoesNotExist:
        autor = None

    if autor:
        if request.method == 'POST':
            form = AutorForm(request.POST, instance=autor)
            if form.is_valid():
                form.save()
                return render(request,'Aplicacion/inicio.html')
        else:
            form = AutorForm(instance=autor)
    else:
        # Manejo de autor no encontrado, puedes personalizar esto según tus necesidades
        return render(request, 'Aplicacion/autor_not_found.html')

    return render(request, 'Aplicacion/autor_editar.html', {'form': form, 'autor': autor})

# Vista para eliminar un autor
def eliminar_autor(request, nombre_autor):
        autor = Autor.objects.get(nombre=nombre_autor)
        if request.method == 'POST':
            # Procesar la eliminación del autor
            autor.delete()
            return render(request,'Aplicacion/inicio.html')
        return render(request, 'Aplicacion/autor_eliminar.html', {'autor': autor})
    

# Vistas para los otros modelos: Genero, Libro y Resena
# Crear, ver lista, editar y eliminar vistas para cada uno de ellos

# Vista para crear un género
def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Aplicacion/inicio.html')
    else:
        form = GeneroForm()
    return render(request, 'Aplicacion/genero_crear.html', {'form': form})

# Vista para ver la lista de géneros
def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'Aplicacion/generos_lista.html', {'generos': generos})

# Vista para editar un género
def editar_genero(request, nombre_genero):
    try:
        genero = Genero.objects.get(nombre=nombre_genero)
    except Genero.DoesNotExist:
        genero = None

    if genero:
        if request.method == 'POST':
            form = GeneroForm(request.POST, instance=genero)
            if form.is_valid():
                form.save()
                return render(request,'Aplicacion/inicio.html')
        else:
            form = GeneroForm(instance=genero)
    else:
        # Manejo de género no encontrado, puedes personalizar esto según tus necesidades
        return render(request, 'Aplicacion/genero_not_found.html')

    return render(request, 'Aplicacion/genero_editar.html', {'form': form, 'genero': genero})

# Vista para eliminar un género
def eliminar_genero(request, nombre_genero):
    genero = Genero.objects.get(nombre=nombre_genero)
    if genero:
        if request.method == 'POST':
            genero.delete()
            return render(request, 'Aplicacion/inicio.html')
        return render(request, 'Aplicacion/genero_eliminar.html', {'genero': genero})
    else:
        # Manejo de género no encontrado, puedes personalizar esto según tus necesidades
        return render(request, 'Aplicacion/genero_not_found.html')

# Vista para crear un libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Aplicacion/inicio.html')
    else:
        form = LibroForm()
    return render(request, 'Aplicacion/libro_crear.html', {'form': form})

# Vista para ver la lista de libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'Aplicacion/libros_lista.html', {'libros': libros})

# Vista para editar un libro
def editar_libro(request, titulo_libro):
    try:
        libro = Libro.objects.get(titulo=titulo_libro)
    except Libro.DoesNotExist:
        libro = None
    if libro:
        if request.method == 'POST':
            form = LibroForm(request.POST, instance=libro)
            if form.is_valid():
                form.save()
                return render(request,'Aplicacion/inicio.html')
        else:
            form = LibroForm(instance=libro)
    else:
        # Manejo de libro no encontrado, puedes personalizar esto según tus necesidades
        return render(request, 'Aplicacion/libro_not_found.html')
    return render(request, 'Aplicacion/libro_editar.html', {'form': form, 'libro': libro})


# Vista para eliminar un libro
def eliminar_libro(request, titulo_libro):
        libro = Libro.objects.get(titulo=titulo_libro)
        if request.method == 'POST':
            # Procesar la eliminación del libro
            libro.delete()
            return render(request,'Aplicacion/inicio.html')
        return render(request, 'Aplicacion/libro_eliminar.html', {'libro': libro})




# SESIONES USUARIO
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "Aplicacion/inicio.html")  # Redirige a la página de perfil o donde desees
            else:
                # Autenticación fallida, muestra un mensaje de error
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'Aplicacion/iniciar_sesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return render(request, "Aplicacion/inicio.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return render(request,"Aplicacion/inicio.html", {"message":"El nuevo usuario fue creado exitosamente!"})
    else:
        form = CustomUserCreationForm()
    return render(request, 'Aplicacion/registro.html', {'form': form})


def perfil(request):
    return render(request, 'Aplicacion/perfil.html')




@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user, )
        if form.is_valid():
            form.save()
            return render(request, "Aplicacion/inicio.html")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'Aplicacion/editar_perfil.html', {'form': form})

@login_required
def eliminar_perfil(request):
    if request.method == 'POST':
        # Agrega una confirmación adicional si es necesario, por ejemplo, solicitando la contraseña actual
        request.user.delete()  # Elimina la cuenta del usuario
        logout(request)  # Cierra la sesión del usuario después de eliminar la cuenta
        return render(request, "Aplicacion/inicio.html")
    return render(request, 'Aplicacion/eliminar_perfil.html')

def about(request):
    return render(request, 'Aplicacion/about.html')