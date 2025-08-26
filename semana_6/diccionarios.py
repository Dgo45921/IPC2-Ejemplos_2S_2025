# diccionarios.py
# Ejemplos con diccionarios

def diccionarios():
    persona = {
        "nombre": "Carlos",
        "edad": 30,
        "profesion": "Ingeniero"
    }
    print("Diccionario inicial:", persona)

    print("Nombre:", persona["nombre"])
    print("Edad (con get):", persona.get("edad"))

    persona["edad"] = 31
    persona["pais"] = "Guatemala"
    print("Diccionario modificado:", persona)

    print("Claves:", list(persona.keys()))
    print("Valores:", list(persona.values()))
    print("Items:", list(persona.items()))

    persona.pop("profesion")
    # del persona["profesion"]  # Alternativa
    print("Después de pop:", persona)
    persona.clear()
    print("Después de clear:" )

def main():
    diccionarios()
main()
