# listas_nativas.py

def funciones_listas():
    numeros = [5, 2, 9, 1, 7]
    print("Lista original:", numeros)

    # len
    print("len(lista):", len(numeros))

    # max
    print("max(lista):", max(numeros))

    # min
    print("min(lista):", min(numeros))

    # sum
    print("sum(lista):", sum(numeros))

    # sorted
    print("sorted(lista):", sorted(numeros))
    print("sorted(lista, reverse=True):", sorted(numeros, reverse=True))


def metodos_listas():
    frutas = ["manzana", "banana", "cereza"]
    print("\nLista original:", frutas)

    # append(elemento)
    frutas.append("naranja")
    print("append('naranja'):", frutas)

    # insert(indice, elemento)
    frutas.insert(1, "kiwi")
    print("insert(1, 'kiwi'):", frutas)

    # remove(elemento)
    frutas.remove("banana")
    print("remove('banana'):", frutas)

    # pop(indice) -> si no se da índice, elimina el último
    frutas.pop()  
    print("pop():", frutas)

    # count(elemento)
    frutas.append("manzana")
    frutas.append("manzana")
    print("count('manzana'):", frutas.count("manzana"))

    # sort(reverse=False)
    frutas.sort()
    print("sort():", frutas)

    frutas.sort(reverse=True)
    print("sort(reverse=True):", frutas)

    # reverse()
    frutas.reverse()
    print("reverse():", frutas)

    # clear()
    frutas.clear()
    print("clear():", frutas)



print("=== Funciones de listas ===")
funciones_listas()

print("\n=== Métodos de listas ===")
metodos_listas()
