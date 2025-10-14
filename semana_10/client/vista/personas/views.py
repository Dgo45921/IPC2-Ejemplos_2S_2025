from django.shortcuts import render
from xml.etree import ElementTree
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    # Obtener el XML desde el servidor
    personas_xml = requests.get('http://localhost:5000/personas/').content
    root = ElementTree.fromstring(personas_xml)

    # Procesar el XML en una lista de diccionarios
    personas = []
    for persona in root.findall('persona'):
        persona_data = {
            'id': persona.find('id').text,
            'nombre': persona.find('nombre').text,
            'edad': persona.find('edad').text,
            'mascotas': []
        }

        mascotas = persona.find('mascotas')
        if mascotas is not None:
            for mascota in mascotas.findall('mascota'):
                mascota_data = {
                    'nombre': mascota.find('nombre').text,
                    'tipo': mascota.find('tipo').text,
                    'foto': mascota.find('foto').text
                }
                persona_data['mascotas'].append(mascota_data)

        personas.append(persona_data)

    # Pasar los datos procesados al contexto de la plantilla
    return render(request, 'index.html', {'personas': personas})


@csrf_exempt
def crear(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        persona_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')

        # Crear el XML
        persona_xml = f"""
        <persona>
            <id>{persona_id}</id>
            <nombre>{nombre}</nombre>
            <edad>{edad}</edad>
        </persona>
        """

        print("XML generado:", persona_xml)  # Depuración

        # Enviar el XML al servidor
        response = requests.post(
            'http://127.0.0.1:5000/personas/crear',
            data=persona_xml,
            headers={'Content-Type': 'application/xml'}
        )

        # Manejar la respuesta del servidor
        if response.status_code == 200:
            return HttpResponse('Persona creada exitosamente', status=200)
        else:
            return HttpResponse('Error al crear la persona', status=response.status_code)

    return render(request, 'nuevaPersona.html')

@csrf_exempt
def nueva_mascota(request):
    if request.method == 'POST':
        print("Formulario de mascota recibido con método POST")  # Depuración
        # Obtener los datos del formulario
        persona_id = request.POST.get('persona_id')
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        foto = request.POST.get('foto')

        # Crear el XML
        mascota_xml = f"""
        <mascota>
            <nombre>{nombre}</nombre>
            <tipo>{tipo}</tipo>
            <foto>{foto}</foto>
        </mascota>
        """

        print("XML de mascota generado:", mascota_xml)  # Depuración

        # Enviar el XML al servidor
        response = requests.post(
            f'http://localhost:5000/personas/{persona_id}/agregar_mascota',
            data=mascota_xml,
            headers={'Content-Type': 'application/xml'}
        )

        # Manejar la respuesta del servidor
        if response.status_code == 200:
            return HttpResponse('Mascota agregada exitosamente', status=200)
        else:
            return HttpResponse('Error al agregar la mascota', status=response.status_code)

    return render(request, 'nuevaMascota.html')