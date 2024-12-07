from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages  # Para mostrar notificaciones 
from django import forms
from .models import Libro
from django.utils import timezone
from django.db.models import Q


# Formulario para agregar libros
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']

# Vista de saludo inicial
def saludo(request):
    return HttpResponse("""
    <html>
    <body>
    <h1>Hola, bienvenido a la librería</h1>
    </body>
    </html>
    """)

# Mostrar registros
def lista_libros(request):
    libros = Libro.objects.all()  # Obtener todos los libros
    return render(request, 'lista_libros.html', {'libros': libros})

# Insertar registro
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.publicado = timezone.now().date()  
            libro.save()
            messages.success(request, "Libro agregado Exitosamente.")
            return redirect('agregar_libro')
        else:
            messages.error(request, "Error al guardar el libro.")
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})
#Buscar libros
def buscar_libro(request):
    query_titulo = request.GET.get('titulo', '').strip()  
    query_autor = request.GET.get('autor', '').strip()    
    
    libros = None  # Variable para almacenar resultados 
    mensaje = None  o

    if query_titulo or query_autor:
        # Filtrar libros según el título y/o autor usando Q 
        libros = Libro.objects.filter(
            Q(titulo__icontains=query_titulo) & Q(autor__icontains=query_autor)
        )

        if not libros:
            mensaje = "No se encontraro el Libro."

    return render(request, 'buscar_libro.html', {
        'libros': libros,
        'query_titulo': query_titulo,
        'query_autor': query_autor,
        'mensaje': mensaje  
    })
    
# Enviar email
def enviar_email(request):
    if request.method == 'POST':
        try:
            send_mail(
                subject='¡Nuevo Libro Agregado!',
                message='Se ha agregado un nuevo libro a la biblioteca.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['smallfati.2310@gmail.com'],  # Dirección de correo del destinatario
            )
            messages.success(request, "Correo enviado con éxito.")
        except Exception as e:
            messages.error(request, f"Error al enviar el correo: {e}")
        return render(request, 'enviar_email.html')
    return render(request, 'enviar_email.html')



