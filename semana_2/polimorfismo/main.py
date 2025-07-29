from Perro import Perro
from Gato import Gato
from Vaca import Vaca

def imprimir_sonido(animal):
    print(animal.hacer_sonido())

def main():
    animales = [Perro(), Gato(), Vaca()]
    for animal in animales:
        imprimir_sonido(animal)

main()