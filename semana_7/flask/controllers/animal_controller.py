from models.lista_enlazada import ListaEnlazada
from models.animal import Animal

lista = ListaEnlazada()

def crear_animal(nombre, especie):
    animal = Animal(nombre, especie)
    lista.agregar(animal)

def eliminar_animal(nombre):
    return lista.eliminar(nombre)

def actualizar_animal(nombre, nuevo_nombre, nueva_especie):
    nuevo_animal = Animal(nuevo_nombre, nueva_especie)
    return lista.actualizar(nombre, nuevo_animal)

def obtener_animales():
    return lista.listar()
