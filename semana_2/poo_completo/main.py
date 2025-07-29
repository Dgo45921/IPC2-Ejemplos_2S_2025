"""
Este programa simula un zoológico utilizando los pilares de la Programación Orientada a Objetos (POO):

1. **Abstracción**: Se define una clase abstracta `Animal` que representa las características y comportamientos generales de un animal.
2. **Encapsulamiento**: Los atributos `__nombre` y `__edad` de la clase `Animal` están encapsulados y se acceden mediante métodos `get_nombre` y `get_edad`.
3. **Herencia**: Las clases `Leon`, `Tigre` y `Elefante` heredan de la clase base `Animal` y definen comportamientos específicos.
4. **Polimorfismo**: Se utiliza el polimorfismo para invocar los métodos `sonido` y `costo_mantenimiento` de diferentes animales de manera uniforme.

El objetivo es demostrar cómo los pilares de la POO pueden ser aplicados para modelar un sistema realista y flexible.
"""

from Leon import Leon
from Tigre import Tigre
from Elefante import Elefante

def main():
    # Crear instancias de diferentes animales
    leon = Leon("Simba", 5)
    tigre = Tigre("Shere Khan", 7)
    elefante = Elefante("Dumbo", 10)

    # Lista de animales
    animales = [leon, tigre, elefante]

    # Mostrar información de cada animal
    for animal in animales:
        print(f"Nombre: {animal.get_nombre()}")
        print(f"Edad: {animal.get_edad()} años")
        print(f"Sonido: {animal.sonido()}")
        print(f"Costo de mantenimiento: ${animal.costo_mantenimiento()} al mes")
        print("-" * 30)

main()