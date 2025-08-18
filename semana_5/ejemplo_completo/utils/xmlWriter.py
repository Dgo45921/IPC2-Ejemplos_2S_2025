import xml.etree.ElementTree as ET
from xml.dom import minidom


def exportar_alumnos_xml(facultades):
    root = ET.Element('universidad')
    facultades_elem = ET.SubElement(root, 'facultades')
    actual_facultad = facultades.primero
    while actual_facultad is not None:
        facultad = actual_facultad.facultad
        fac_elem = ET.SubElement(facultades_elem, 'facultad', {'id': str(facultad.id)})
        nombre_elem = ET.SubElement(fac_elem, 'nombre')
        nombre_elem.text = facultad.nombre
        alumnos_elem = ET.SubElement(fac_elem, 'alumnos')
        if hasattr(facultad, 'alumnos') and facultad.alumnos is not None:
            actual_alumno = facultad.alumnos.primero
            while actual_alumno is not None:
                alumno = actual_alumno.alumno
                alumno_elem = ET.SubElement(alumnos_elem, 'alumno', {'id': str(alumno.id)})
                nombre_alum = ET.SubElement(alumno_elem, 'nombre')
                nombre_alum.text = alumno.nombre
                correo_alum = ET.SubElement(alumno_elem, 'correo')
                correo_alum.text = alumno.correo
                edad_alum = ET.SubElement(alumno_elem, 'edad')
                edad_alum.text = str(alumno.edad)
                actual_alumno = actual_alumno.siguiente
        actual_facultad = actual_facultad.siguiente
    xml_str = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
    with open('alumnos_exportados.xml', 'w+', encoding='utf-8') as f:
        f.write(pretty_xml)