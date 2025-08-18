from Nodo import Nodo

class NodoAnimal(Nodo):
    def __init__(self, animal, siguiente=None):
        super().__init__(siguiente)
        self.animal = animal

    def __str__(self):
        return f"NodoAnimal: {self.animal}"
