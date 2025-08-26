# Ejemplo de mutabilidad en objetos tipo dict

def update_price(product, new_price):
    product["price"] = new_price

product_a = {"name": "Laptop", "price": 1200}
update_price(product_a, 1000)

print("Producto mutable actualizado:", product_a)
# Salida: {'name': 'Laptop', 'price': 1000}


# Ejemplo con objeto inmutable (int)

def update_price(price, new_price):
    price = new_price  # No cambia el valor original

price_a = 1200
update_price(price_a, 1000)

print("Precio inmutable:", price_a)
# Salida: 1200


# Ejemplo de problema clásico con lista como valor por defecto

def agregar_elemento(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(agregar_elemento(1))  # [1]
print(agregar_elemento(2))  # [1, 2] — no esperado si se quería una lista nueva


# solucion recomendada
def agregar_elemento(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista


print(id(1))