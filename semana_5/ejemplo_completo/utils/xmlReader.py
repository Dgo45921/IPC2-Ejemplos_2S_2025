import xml.etree.ElementTree as ET
from entities.Facultad import Facultad
from entities.Carrera import Carrera
from entities.Alumno import Alumno
from entities.Profesor import Profesor
from TDA.ListaFacultad import ListaFacultad





def leer_universidad_xml(path):
    facultades = ListaFacultad()

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        facultades_elem = root.find('facultades')
        for fac_elem in facultades_elem.findall('facultad'):
            id_facultad = int(fac_elem.get('id'))
            nombre_facultad = fac_elem.find('nombre').text
            facultad = Facultad(id_facultad, nombre_facultad)

            # Carreras
            for carrera_elem in fac_elem.findall('carrera'):
                id_carrera = int(carrera_elem.get('id'))
                nombre_carrera = carrera_elem.text
                carrera = Carrera(id_carrera, nombre_carrera)
                facultad.carreras.insertar(carrera)

            # Personas: profesores
            personas_elem = fac_elem.find('personas')
            if personas_elem is not None:
                for profesor_elem in personas_elem.findall('profesor'):
                    id_profesor = int(profesor_elem.get('id'))
                    nombre_profesor = profesor_elem.find('nombre').text
                    correo_profesor = profesor_elem.find('correo').text
                    profesor = Profesor(id_profesor, nombre_profesor, correo_profesor)
                    facultad.docentes.insertar(profesor)

                # Personas: estudiantes
                for estudiante_elem in personas_elem.findall('estudiante'):
                    id_estudiante = int(estudiante_elem.get('id'))
                    nombre_estudiante = estudiante_elem.find('nombre').text
                    correo_estudiante = estudiante_elem.find('correo').text
                    edad_estudiante = int(estudiante_elem.find('edad').text)
                    alumno = Alumno(id_estudiante, nombre_estudiante, correo_estudiante, edad_estudiante)
                    facultad.alumnos.insertar(alumno)   

            for docente_elem in fac_elem.findall('docentes/docente'):
                id_docente = int(docente_elem.get('id'))
                nombre_docente = docente_elem.find('nombre').text
                correo_docente = docente_elem.find('correo').text
                edad_docente = int(docente_elem.find('edad').text)
                docente = Profesor(id_docente, nombre_docente, correo_docente, edad_docente)
                facultad.docentes.insertar(docente)

            facultades.insertar(facultad)

        return facultades

    except ET.ParseError as e:
        print(f"Error al parsear el XML: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
