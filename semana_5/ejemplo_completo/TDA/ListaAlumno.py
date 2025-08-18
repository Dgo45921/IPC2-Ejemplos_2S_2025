
from TDA.NodoAlumno import NodoAlumno

class ListaAlumno:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def insertar(self, alumno):
        nuevo_nodo = NodoAlumno(alumno)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.size += 1

    def __str__(self):
        resultado = []
        actual = self.primero
        while actual is not None:
            alumno = actual.alumno
            resultado.append(f"{alumno.id} - {alumno.nombre} - {alumno.correo} - {alumno.edad}")
            actual = actual.siguiente
        return "\n".join(resultado)