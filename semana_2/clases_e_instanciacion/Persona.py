class Persona:
    def __init__(self, nombre, edad, casado=False):
        self.nombre = nombre
        self.edad = edad
        self.casado = casado

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def decir_si_estoy_casado(self):
        return "Estoy casado." if self.casado else "No estoy casado."