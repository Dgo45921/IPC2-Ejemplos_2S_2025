from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
dictionary = {
    'nombre': 'Alumnos IPC2',
    'alumnos': [
        {
            'nombre': 'Luis',
            'edad': 20
        },
        {
            'nombre': 'Javier',
            'edad': 21
        },
        {
            'nombre': 'Andrea',
            'edad': 19
        }
    ]
    }

def index(request):
    return HttpResponse("Hola mundo desde Django")



def lista_alumnos(request):
    return HttpResponse(json.dumps(dictionary), content_type='application/json')
