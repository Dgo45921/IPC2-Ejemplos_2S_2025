class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.mascotas = []  

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
