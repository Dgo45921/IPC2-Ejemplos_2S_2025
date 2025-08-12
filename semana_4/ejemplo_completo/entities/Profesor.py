from entities.Persona import Persona


class Profesor(Persona):
    def __init__(self, id, nombre, correo):
        super().__init__(id, nombre, correo)
        

    def __str__(self):
        return f"Profesor: {self.nombre}, Correo: {self.correo}, ID: {self.id}"
