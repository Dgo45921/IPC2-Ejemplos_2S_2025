from TDA.ListaAlumno import ListaAlumno
from TDA.ListaProfesor import ListaProfesor
from TDA.ListaCarrera import ListaCarrera


class Facultad:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.carreras = ListaCarrera()
        self.alumnos = ListaAlumno()
        self.docentes = ListaProfesor()

    