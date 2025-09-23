import json
import requests  # para ejemplo con APIs e HTTP (internet como origen de datos)

# ---------------------------
# 1. Sintaxis básica de JSON
# ---------------------------
json_string = '''
{
    "nombre": "Diego",
    "edad": 22,
    "activo": true,
    "cursos": ["Python", "JavaScript", "Bases de Datos"],
    "direccion": {
        "ciudad": "Guatemala",
        "codigo_postal": null
    }
}
'''

print("=== Ejemplo de JSON en texto ===")
print(json_string)

# ---------------------------
# 2. Convertir JSON -> Diccionario
# ---------------------------
data = json.loads(json_string)
print("\n=== JSON a diccionario de Python ===")
print(data)
print("Nombre:", data["nombre"])
print("Cursos:", data["cursos"])

# ---------------------------
# 3. Convertir Diccionario -> JSON
# ---------------------------
dict_python = {
    "lenguaje": "Python",
    "version": 3.11,
    "es_popular": True,
    "competidores": ["Java", "C#", "JavaScript"],
    "creador": None
}

json_generado = json.dumps(dict_python, indent=4)
print("\n=== Diccionario a JSON ===")
print(json_generado)

# ---------------------------
# 4. Convertir otros tipos a JSON
# ---------------------------
lista = [1, 2, 3, "texto", True, None]
tupla = ("A", "B", "C")

print("\n=== Listas y Tuplas a JSON ===")
print("Lista:", json.dumps(lista))
print("Tupla:", json.dumps(tupla))

# ---------------------------
# 5. Diferencias JSON vs XML
# ---------------------------
print("\n=== Comparación rápida JSON vs XML ===")
print("JSON: más ligero, clave-valor, fácil de usar con APIs REST")
print("XML: más verboso, jerárquico, usado en documentos complejos")

# ---------------------------
# 6. Ejemplo práctico: Internet como origen de datos (API)
# ---------------------------
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    if response.status_code == 200:
        usuario = response.json()
        print("\n=== Datos obtenidos de una API ===")
        print("Nombre:", usuario["name"])
        print("Email:", usuario["email"])
        print("Ciudad:", usuario["address"]["city"])
    else:
        print("Error en la petición HTTP:", response.status_code)
except Exception as e:
    print("No se pudo conectar a la API:", e)

# ---------------------------
# 7. Tipos de datos JSON
# ---------------------------
ejemplo_tipos = {
    "matriz": [1, 2, 3],
    "booleano": False,
    "nulo": None,
    "numero": 42.5,
    "cadena": "Hola JSON"
}
print("\n=== Tipos de datos JSON en Python ===")
print(json.dumps(ejemplo_tipos, indent=4))
