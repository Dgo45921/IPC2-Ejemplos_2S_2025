class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self):
        return f"Animal(nombre={self.nombre}, especie={self.especie})"