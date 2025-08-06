# Ejemplo 1: Funcion sin parámetros y sin valor de retorno
def greet():
    print("Hello, world!")

# Ejemplo 2: Funcion con parámetros y sin valor de retorno
def print_sum(a, b):
    print("The sum is:", a + b)

# Ejemplo 3: Funcion con parámetros y valor de retorno
def multiply(x, y):
    return x * y

# Ejemplo 4: funcion con un parámetro con valor por defecto
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

# Ejemplo 5: Funcion que verifica si un número es par y retorna un valor booleano
def is_even(number):
    return number % 2 == 0


greet()
print_sum(10,5)
print(multiply(2,2))
say_hello()
print(is_even(4))