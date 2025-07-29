from Vehiculo import Vehiculo

class Barco(Vehiculo):
    def __init__(self, medio, marca, color, millas_nauticas_recorridas):
        super().__init__(medio, marca, color)
        self.millas_nauticas_recorridas = millas_nauticas_recorridas

    def obtener_millas_nauticas_recorridas(self):
        return self.millas_nauticas_recorridas