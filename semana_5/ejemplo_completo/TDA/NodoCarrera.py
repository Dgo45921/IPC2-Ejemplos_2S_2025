from TDA.Nodo import Nodo



class NodoCarrera(Nodo):
    def __init__(self, carrera, siguiente=None):
        super().__init__(siguiente)
        self.carrera = carrera

    def __str__(self):
        return f"NodoCarrera: {self.carrera}"
