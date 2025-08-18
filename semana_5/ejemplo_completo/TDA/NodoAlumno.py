from TDA.Nodo import Nodo


class NodoAlumno(Nodo):
    def __init__(self, alumno, siguiente=None):
        super().__init__(siguiente)
        self.alumno = alumno

    def __str__(self):
        return f"NodoAlumno: {self.alumno}"