from TDA.NodoCarrera import NodoCarrera


class ListaCarrera:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def insertar(self, carrera):
        nuevo_nodo = NodoCarrera(carrera)
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
            carrera = actual.carrera
            resultado.append(f"{carrera.id} - {carrera.nombre}")
            actual = actual.siguiente
        return "\n".join(resultado)