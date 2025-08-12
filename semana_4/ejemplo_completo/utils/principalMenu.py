from utils.xmlReader import leer_universidad_xml
from utils.xmlWriter import exportar_alumnos_xml

facultades = []

def mostrar_estudiantes(facultades):
    if not facultades:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Estudiantes ---")
    for facultad in facultades:
        for alumno in facultad.alumnos:
            print(f"Facultad: {facultad.nombre} | {alumno}")

def mostrar_docentes(facultades):
    if not facultades:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Docentes ---")
    for facultad in facultades:
        for docente in facultad.docentes:
            print(f"Facultad: {facultad.nombre} | {docente}")

def mostrar_carreras(facultades):
    if not facultades:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Carreras ---")
    for facultad in facultades:
        for carrera in facultad.carreras:
            print(f"Facultad: {facultad.nombre} | Carrera: {carrera.nombre} (ID: {carrera.id})")

def mostrar_facultades(facultades):
    if not facultades:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Facultades ---")
    for facultad in facultades:
        print(f"Facultad: {facultad.nombre} (ID: {facultad.id})")

def showMenu():

    print("==== BIENVENIDO A MI MINI UNIVERSIDAD ====")
    print("1. Carga masiva XML")
    print("2. Ver estudiantes")
    print("3. Ver docentes")
    print("4. Ver carreras")
    print("5. Ver facultades")
    print("6. Exportar alumnos a XML")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    while opcion != '7':
        if opcion == '1':
            path_xml = input("Ingrese la ruta del archivo XML: ")
            print(f"Cargando datos desde {path_xml}...")
            global facultades
            facultades = leer_universidad_xml(path_xml)

        elif opcion == '2':
            print("Mostrando estudiantes...")
            mostrar_estudiantes(facultades)
        elif opcion == '3':
            print("Mostrando docentes...")
            mostrar_docentes(facultades)
        elif opcion == '4':
            print("Mostrando carreras...")
            mostrar_carreras(facultades)
        elif opcion == '5':
            print("Mostrando facultades...")
            mostrar_facultades(facultades)
        elif opcion == '6':
            print("Exportando alumnos a XML...")
            exportar_alumnos_xml(facultades)

        else:
            print("Opción no válida. Intente de nuevo.")

        
        print("==== BIENVENIDO A MI MINI UNIVERSIDAD ====")
        print("1. Carga masiva XML")
        print("2. Ver estudiantes")
        print("3. Ver docentes")
        print("4. Ver carreras")
        print("5. Ver facultades")
        print("6. Exportar alumnos a XML")
        print("7. Salir")


        opcion = input("Seleccione una opción: ")
