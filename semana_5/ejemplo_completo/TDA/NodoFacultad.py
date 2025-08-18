from TDA.Nodo import Nodo


class NodoFacultad(Nodo):
    def __init__(self, facultad, siguiente=None):
        super().__init__(siguiente)
        self.facultad = facultad
        
    def __str__(self):
        return f"NodoFacultad: {self.facultad}"

