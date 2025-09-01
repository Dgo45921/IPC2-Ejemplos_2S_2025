class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal):
        nuevo = Nodo(animal)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.animal.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def actualizar(self, nombre, nuevo_animal):
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre:
                actual.animal = nuevo_animal
                return True
            actual = actual.siguiente
        return False

    def __iter__(self):
        self._iter_actual = self.cabeza
        return self

    def __next__(self):
        if self._iter_actual is None:
            raise StopIteration
        animal = self._iter_actual.animal
        self._iter_actual = self._iter_actual.siguiente
        return animal