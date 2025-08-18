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
        if not actual:
            return False
        while True:
            if actual.animal.nombre == animal.nombre:
                if self.size == 1:
                    self.primero = self.ultimo = None
                else:
                    if actual == self.primero:
                        # primer nodo
                        self.primero = actual.siguiente
                        self.ultimo.siguiente = self.primero
                        self.primero.anterior = self.ultimo
                    elif actual == self.ultimo:
                        # ultimo nodo
                        self.ultimo = actual.anterior
                        self.ultimo.siguiente = self.primero
                        self.primero.anterior = self.ultimo
                    else:
                        # nodo intermedio
                        actual.anterior.siguiente = actual.siguiente
                        actual.siguiente.anterior = actual.anterior
                self.size -= 1
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
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
        
