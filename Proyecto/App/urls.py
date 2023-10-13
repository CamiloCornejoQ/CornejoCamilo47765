from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    
    # URLs para Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<nombre_autor>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<nombre_autor>>/', views.eliminar_autor, name='eliminar_autor'),
   

   # URLs para Generos
    path('generos/', views.lista_generos, name='lista_generos'),
    path('generos/crear/', views.crear_genero, name='crear_genero'),
    path('generos/editar/<nombre_genero>/', views.editar_genero, name='editar_genero'),
    path('generos/eliminar/<nombre_genero>/', views.eliminar_genero, name='eliminar_genero'),

    # URLs para Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<titulo_libro>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<titulo_libro>/', views.eliminar_libro, name='eliminar_libro'),

    # URLs para Sobre
    path('about', views.about, name='about'),
    # URLs para Buscar
    #path('buscar', views.buscar, name='buscar'),

    # URLs para Usuarios
    path('Registro', views.register, name='registro'),
    path('iniciarsesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('perfil', views.perfil, name='perfil'),
    path('perfileditar', views.editar_perfil, name='editar_perfil'),
    path('perfileliminar', views.eliminar_perfil, name='eliminar_perfil'),
    path('cerrarsesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('cambiarcontrasena', views.CambiarContraseñaView.as_view(), name='cambiar_contrasena'),
]

