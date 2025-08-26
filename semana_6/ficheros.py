# ficheros.py
# Ejemplos de manejo de ficheros en Python


path_archivo = "C:/Users/Dgo/Documents/IPC2/semana_6/datos.txt"
path_lorem_ipsum = "C:/Users/Dgo/Documents/IPC2/semana_6/lorem_ipsum.txt"
path_encodings = "C:/Users/Dgo/Documents/IPC2/semana_6/encodings.txt"

def escribir_archivo():
    with open(path_archivo, "w", encoding="utf-8") as f:
        f.write("Hola, este es un ejemplo de escritura en ficheros.\n")
        f.write("Cada ejecución sobrescribe el contenido.\n")

def leer_completo():
    with open(path_lorem_ipsum, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("[LECTURA COMPLETA]\n", contenido)

def leer_lineas():
    with open(path_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            print("[LINEA]", linea.strip())

def anadir_archivo():
    with open(path_archivo, "a", encoding="utf-8") as f:
        f.write("Nueva línea añadida sin borrar lo anterior.\n")

def manejo_errores():
    try:
        with open("C:/Users/Dgo/Documents/IPC2/semana_6/no_existe.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: El fichero no existe.")

def encodings():
    with open(path_encodings, "r", encoding="utf-8") as f:
        contenido = f.read()
    print(contenido)



def main():
    # escribir_archivo()
    # leer_completo()
    # leer_lineas()
    encodings()
    # anadir_archivo()
    # manejo_errores()

main()