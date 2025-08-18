from Nodo import Nodo

class NodoAnimal(Nodo):
    def __init__(self, animal, siguiente=None, anterior=None):
        super().__init__(siguiente)
        self.animal = animal
        self.anterior = anterior

    def __str__(self):
        return f"NodoAnimal: {self.animal}"
