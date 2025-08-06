# Ejemplo 1: Sentencia if simple
numero = 10
# Verifica si el número es mayor que 5
if numero > 5:
    print("El número es mayor que 5")
    if numero == 10:
        print("el numero es 10")



# Ejemplo 2: if-else
usuario = "admin"
# Verifica si el usuario es administrador
if usuario == "admin":
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Ejemplo 3: if-elif-else


edad = 15
# Clasifica la edad en categorías
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
