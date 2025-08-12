class Persona():
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}"