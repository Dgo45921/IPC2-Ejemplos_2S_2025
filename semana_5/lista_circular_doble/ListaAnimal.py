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
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.size += 1

    def buscar(self, animal):
        actual = self.primero
        if not actual:
            return None
        while True:
            if actual.animal.nombre == animal.nombre:
                return actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        return None

    def eliminar(self, animal):
        actual = self.primero

        # lista vacia
        if actual is None:
            return False
        
        # es el primer nodo el que se quiere eliminar
        if actual.animal.nombre == animal.nombre:
            self.primero = actual.siguiente
            actual.siguiente.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            actual.siguiente = None
            actual.anterior = None
            self.size -= 1
            return True
        
        # es un nodo intermedio o final
        while actual:
            if actual.animal.nombre == animal.nombre:
                if actual == self.ultimo: # nodo final
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente = self.primero
                    actual.anterior = None
                    self.primero.anterior = self.ultimo
                    actual.siguiente = None
                    
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
        if not actual:
            return
        while True:
            print(f"Nombre: {actual.animal.nombre}, Especie: {actual.animal.especie}")
            actual = actual.siguiente
            if actual == self.primero:
                break
        
