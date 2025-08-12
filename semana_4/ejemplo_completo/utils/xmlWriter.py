import xml.etree.ElementTree as ET
from xml.dom import minidom


def exportar_alumnos_xml(facultades):
    root = ET.Element('universidad')
    facultades_elem = ET.SubElement(root, 'facultades')
    for facultad in facultades:
        fac_elem = ET.SubElement(facultades_elem, 'facultad', {'id': str(facultad.id)})
        nombre_elem = ET.SubElement(fac_elem, 'nombre')
        nombre_elem.text = facultad.nombre
        alumnos_elem = ET.SubElement(fac_elem, 'alumnos')
        for alumno in facultad.alumnos:
            alumno_elem = ET.SubElement(alumnos_elem, 'alumno', {'id': str(alumno.id)})
            nombre_alum = ET.SubElement(alumno_elem, 'nombre')
            nombre_alum.text = alumno.nombre
            correo_alum = ET.SubElement(alumno_elem, 'correo')
            correo_alum.text = alumno.correo
            edad_alum = ET.SubElement(alumno_elem, 'edad')
            edad_alum.text = str(alumno.edad)
    xml_str = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
    with open('alumnos_exportados.xml', 'w+', encoding='utf-8') as f:
        f.write(pretty_xml)