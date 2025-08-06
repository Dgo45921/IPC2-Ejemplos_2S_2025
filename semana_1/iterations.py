# Ejemplos básicos de iteraciones en Python


# 1. Iterar sobre una lista usando for
frutas = ["manzana", "banana", "cereza"]
print("Ejemplo 1: Iterar sobre una lista")
for fruta in frutas:
    print(fruta)

# 2. Usar range para imprimir números del 0 al 4
print("\nEjemplo 2: Usar range en un for")
for i in range(1,5):
    print(i)

# 3. Iterar sobre los caracteres de una cadena
texto = "Hola"
print("\nEjemplo 3: Iterar sobre los caracteres de una cadena")
for letra in texto:
    print(letra)

# 4. Usar while para contar hasta 5
print("\nEjemplo 4: Usar while para contar")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1



edad = input("ingrese su edad")

edad_numero = int(edad)

print(edad_numero+5)