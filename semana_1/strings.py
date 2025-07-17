# Ejemplos básicos de manipulación de cadenas en Python

# 1. Concatenación de cadenas
nombre = "Juan"
apellido = "Guerra"
nombre_completo = nombre + " " + apellido
print("Concatenación:", nombre_completo)

# 2. Convertir a mayúsculas y minúsculas
texto = "Hola Mundo"
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())

# 3. Reemplazar texto en una cadena
frase = "Me gusta programar en Java"
frase_nueva = frase.replace("Java", "Python")
print("Reemplazo:", frase_nueva)

# 4. Dividir una cadena en partes
datos = "manzana,pera,banana"
lista_frutas = datos.split(",")
print("Lista de frutas:", lista_frutas)

# 5. Eliminar espacios al inicio y al final
mensaje = "   Hola, ¿cómo estás?   "
mensaje_limpio = mensaje.strip()
print("Mensaje limpio:", mensaje_limpio)
