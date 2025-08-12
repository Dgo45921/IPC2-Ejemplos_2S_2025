import xml.etree.ElementTree as ET
from entities.Facultad import Facultad
from entities.Carrera import Carrera
from entities.Alumno import Alumno
from entities.Profesor import Profesor

def leer_universidad_xml(path):
    facultades = []
    tree = ET.parse(path)
    root = tree.getroot()
    for fac_elem in root.find('facultades').findall('facultad'):
        id_fac = fac_elem.get('id')
        nombre_fac = fac_elem.find('nombre').text
        facultad = Facultad(id_fac, nombre_fac)
        # Carreras
        for car_elem in fac_elem.findall('carrera'):
            id_car = car_elem.get('id')
            nombre_car = car_elem.text
            carrera = Carrera(id_car, nombre_car)
            facultad.carreras.append(carrera)
        # Personas
        personas_elem = fac_elem.find('personas')
        if personas_elem is not None:
            for prof_elem in personas_elem.findall('profesor'):
                id_prof = prof_elem.get('id')
                nombre_prof = prof_elem.find('nombre').text
                correo_prof = prof_elem.find('correo').text
                profesor = Profesor(id_prof, nombre_prof, correo_prof)
                facultad.docentes.append(profesor)
            for est_elem in personas_elem.findall('estudiante'):
                id_est = est_elem.get('id')
                nombre_est = est_elem.find('nombre').text
                correo_est = est_elem.find('correo').text
                edad_est = int(est_elem.find('edad').text)
                alumno = Alumno(id_est, nombre_est, correo_est, edad_est)
                facultad.alumnos.append(alumno)
        facultades.append(facultad)
    return facultades
