"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import saludo, lista_libros, agregar_libro, enviar_email, buscar_libro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),  # Asocia un nombre a esta URL
    path('lista_libros/', lista_libros, name='lista_libros'),  # Nombre para lista_libros
    path('agregar_libro/', agregar_libro, name='agregar_libro'),  # Aquí está el problema, agrega name
    path('enviar_email/', enviar_email, name='enviar_email'),  # Nombre para enviar_email
    path('buscar_libro/', buscar_libro, name='buscar_libro'),
]

