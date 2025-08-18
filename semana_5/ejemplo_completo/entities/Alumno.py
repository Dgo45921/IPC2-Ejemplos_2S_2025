from entities.Persona import Persona

class Alumno(Persona):
    def __init__(self, id, nombre, correo, edad):
        super().__init__(id, nombre, correo)
        self.edad = edad
        

    def __str__(self):
        return f"Alumno: {self.nombre}, Edad: {self.edad}, ID: {self.id}"