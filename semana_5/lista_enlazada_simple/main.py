
from Animal import Animal
from ListaAnimal import ListaAnimal

def main():
	lista = ListaAnimal()

	# Crear varios animales
	a1 = Animal("Max", "Perro")
	a2 = Animal("Mimi", "Gato")
	a3 = Animal("Dumbo", "Elefante")
	a4 = Animal("Simba", "León")

	# Insertar animales en la lista
	lista.insertar(a1)
	lista.insertar(a2)
	lista.insertar(a3)
	lista.insertar(a4)

	print("Lista de animales:")
	print(lista)

	# Buscar un animal
	print("\nBuscando a Mimi:")
	encontrado = lista.buscar(a2)
	print(encontrado if encontrado else "No encontrado")

	# Eliminar un animal
	print("\nEliminando a Dumbo:")
	eliminado = lista.eliminar(a3)
	print("Eliminado" if eliminado else "No encontrado")
	print(lista)

	# Actualizar un animal
	print("\nActualizando a Simba por Nala:")
	nuevo_animal = Animal("Nala", "León")
	actualizado = lista.actualizar(a4, nuevo_animal)
	print("Actualizado" if actualizado else "No encontrado")
	print(lista)

if __name__ == "__main__":
	main()
