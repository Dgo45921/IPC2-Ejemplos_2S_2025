from django.shortcuts import render, HttpResponse
from .models import Persona

def home(request):
    return HttpResponse("Hola Mundo")

def index(request):
    return render(request, 'index.html')

def saludo(request):
    contexto = {
        'nombre': 'Alumnos IPC2'
    }
    return render(request, 'saludo.html', contexto)

def personas(request):
    personas = Persona.objects.all()
    contexto = {
        'personas': personas
    }
    
    return render(request, 'personas.html', contexto)