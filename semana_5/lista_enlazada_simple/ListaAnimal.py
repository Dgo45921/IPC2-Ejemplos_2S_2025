from NodoAnimal import NodoAnimal

class ListaAnimal:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, animal):
        nuevo = NodoAnimal(animal)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1

    def buscar(self, animal):
        actual = self.primero
        while actual:
            if actual.animal.nombre == animal.nombre:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, animal):
        actual = self.primero
        anterior = None
        while actual:
            if actual.animal.nombre == animal.nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual == self.ultimo:
                    self.ultimo = anterior
                self.size -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def actualizar(self, viejo, nuevo):
        nodo = self.buscar(viejo)
        if nodo:
            nodo.animal = nuevo
            return True
        return False

    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(actual.animal)
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Lista vacía"