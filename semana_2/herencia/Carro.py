from Vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, medio, marca, color, ruedas):
        super().__init__(medio, marca, color)
        self.ruedas = ruedas

    def obtener_ruedas(self):
        return self.ruedas