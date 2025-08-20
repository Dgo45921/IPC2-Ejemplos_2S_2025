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
            nuevo.anterior = self.ultimo
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

        # lista vacia
        if actual is None:
            return False
        
        # es el primer nodo el que se quiere eliminar
        if actual.animal.nombre == animal.nombre:
            self.primero = actual.siguiente
            actual.siguiente.anterior = None
            actual.siguiente = None
            self.size -= 1
            return True
        
        # es un nodo intermedio o final
        while actual:
            if actual.animal.nombre == animal.nombre:
                if actual == self.ultimo: # nodo final
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente = None
                    actual.anterior = None
                else: # nodo intermedio
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.size -= 1
                return True

            actual = actual.siguiente
        return False
            

    def actualizar(self, viejo, nuevo):
        nodo = self.buscar(viejo)
        if nodo:
            nodo.animal = nuevo
            return True
        return False

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"Nombre: {actual.animal.nombre}, Especie: {actual.animal.especie}")
            actual = actual.siguiente
        
