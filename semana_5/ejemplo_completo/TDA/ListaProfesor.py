
from TDA.NodoProfesor import NodoProfesor

class ListaProfesor:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, profesor):
        nuevo_nodo = NodoProfesor(profesor)
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
            profesor = actual.profesor
            resultado.append(f"{profesor.id} - {profesor.nombre} - {profesor.correo}")
            actual = actual.siguiente
        return "\n".join(resultado)