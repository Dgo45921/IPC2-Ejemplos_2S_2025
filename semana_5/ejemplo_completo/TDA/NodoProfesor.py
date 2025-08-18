from TDA.Nodo import Nodo

class NodoProfesor(Nodo):
    def __init__(self, profesor, siguiente=None):
        super().__init__(siguiente)
        self.profesor = profesor

    def __str__(self):
        return f"NodoProfesor: {self.profesor}"