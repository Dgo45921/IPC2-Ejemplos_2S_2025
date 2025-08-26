# tuplas.py
# Ejemplos con tuplas

def tuplas():
    tupla1 = (1, 2, 3)
    # error
    tupla1[0] = 10  # Las tuplas son inmutables
    tupla2 = "a", "b", "c"
    print("Tuplas:", tupla1, tupla2)

    print("Primer elemento:", tupla1[0])

    tupla3 = tupla1 + (4, 5)
    print("Concatenación:", tupla3)
    print("Repetición:", tupla2 * 2)

    coordenadas = {}
    coordenadas[(10, 20)] = "Punto A"
    print("Diccionario con tupla como clave:", coordenadas)

def main():
    tuplas()
main()
