from flask import Blueprint, request, Response
import xml.etree.ElementTree as ET

from models.Persona import Persona
from models.Mascota import Mascota

persona_bp = Blueprint('persona', __name__)

# Lista de personas
personas = []


def personas_to_xml(personas):
    root = ET.Element('personas')
    for persona in personas:
        persona_elem = ET.SubElement(root, 'persona')
        ET.SubElement(persona_elem, 'id').text = str(persona.id)
        ET.SubElement(persona_elem, 'nombre').text = persona.nombre
        ET.SubElement(persona_elem, 'edad').text = str(persona.edad)
        mascotas_elem = ET.SubElement(persona_elem, 'mascotas')
        for mascota in persona.mascotas:
            mascota_elem = ET.SubElement(mascotas_elem, 'mascota')
            ET.SubElement(mascota_elem, 'nombre').text = mascota.nombre
            ET.SubElement(mascota_elem, 'tipo').text = mascota.tipo
            ET.SubElement(mascota_elem, 'foto').text = mascota.foto
    return ET.tostring(root, encoding='utf-8')

@persona_bp.route('/', methods=['GET'])
def index():
    xml_data = personas_to_xml(personas)
    return Response(xml_data, content_type='application/xml')

@persona_bp.route('/crear', methods=['POST'])
def crear():
    xml_data = request.data
    root = ET.fromstring(xml_data)
    id = int(root.find('id').text)
    nombre = root.find('nombre').text
    edad = int(root.find('edad').text)
    nueva_persona = Persona(id, nombre, edad)
    personas.append(nueva_persona)
    return Response("<mensaje>Persona creada</mensaje>", content_type='application/xml')

@persona_bp.route('/<int:id_persona>/agregar_mascota', methods=['POST'])
def agregar_mascota(id_persona):
    xml_data = request.data
    root = ET.fromstring(xml_data)
    nombre_mascota = root.find('nombre').text
    tipo_mascota = root.find('tipo').text
    foto_mascota = root.find('foto').text
    mascota = Mascota(nombre_mascota, tipo_mascota, foto_mascota)

    for persona in personas:
        if persona.id == id_persona:
            persona.agregar_mascota(mascota)
            return Response("<mensaje>Mascota agregada a la persona</mensaje>", content_type='application/xml')

    return Response("<error>Persona no encontrada</error>", content_type='application/xml', status=404)

@persona_bp.route('/editar/<int:id_persona>', methods=['PUT'])
def editar(id_persona):
    xml_data = request.data
    root = ET.fromstring(xml_data)
    nueva_edad = int(root.find('edad').text)
    for persona in personas:
        if persona.id == id_persona:
            persona.edad = nueva_edad
            return Response("<mensaje>Persona actualizada</mensaje>", content_type='application/xml')
    return Response("<error>Persona no encontrada</error>", content_type='application/xml', status=404)

@persona_bp.route('/eliminar/<int:id_persona>', methods=['DELETE'])
def eliminar(id_persona):
    global personas
    personas = [p for p in personas if p.id != id_persona]
    return Response("<mensaje>Persona eliminada</mensaje>", content_type='application/xml')

