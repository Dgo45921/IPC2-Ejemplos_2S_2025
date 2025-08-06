from Circulo import Circulo
from Rectangulo import Rectangulo

# Uso de las clases
def main():

    figuras = [
        Circulo(5),
        Rectangulo(4, 6)]

    for figura in figuras:
        print(f"El área de la figura es: {figura.calcular_area()}")

main()