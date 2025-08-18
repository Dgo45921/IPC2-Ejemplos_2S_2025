from utils.xmlReader import leer_universidad_xml
from utils.xmlWriter import exportar_alumnos_xml
from TDA.ListaFacultad import ListaFacultad


facultades = ListaFacultad()

def mostrar_estudiantes(facultades):
    if facultades is None or facultades.primero is None:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Estudiantes ---")
    actual_facultad = facultades.primero
    while actual_facultad is not None:
        facultad = actual_facultad.facultad
        if facultad.alumnos is not None:
            actual_alumno = facultad.alumnos.primero
            while actual_alumno is not None:
                alumno = actual_alumno.alumno
                print(f"Facultad: {facultad.nombre} | {alumno.id} - {alumno.nombre} - {alumno.correo} - {alumno.edad}")
                actual_alumno = actual_alumno.siguiente
        actual_facultad = actual_facultad.siguiente

def mostrar_docentes(facultades):
    if facultades is None or facultades.primero is None:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Docentes ---")
    actual_facultad = facultades.primero
    while actual_facultad is not None:
        facultad = actual_facultad.facultad
        if facultad.docentes is not None:
            actual_docente = facultad.docentes.primero
            while actual_docente is not None:
                docente = actual_docente.profesor
                print(f"Facultad: {facultad.nombre} | {docente.id} - {docente.nombre} - {docente.correo}")
                actual_docente = actual_docente.siguiente
        actual_facultad = actual_facultad.siguiente

def mostrar_carreras(facultades):
    if facultades is None or facultades.primero is None:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Carreras ---")
    actual_facultad = facultades.primero
    while actual_facultad is not None:
        facultad = actual_facultad.facultad
        if facultad.carreras is not None:
            actual_carrera = facultad.carreras.primero
            while actual_carrera is not None:
                carrera = actual_carrera.carrera
                print(f"Facultad: {facultad.nombre} | Carrera: {carrera.nombre} (ID: {carrera.id})")
                actual_carrera = actual_carrera.siguiente
        actual_facultad = actual_facultad.siguiente

def mostrar_facultades(facultades):
    if facultades is None or facultades.primero is None:
        print("No hay datos cargados. Por favor, cargue el XML primero.")
        return
    print("\n--- Facultades ---")
    actual_facultad = facultades.primero
    while actual_facultad is not None:
        facultad = actual_facultad.facultad
        print(f"Facultad: {facultad.nombre} (ID: {facultad.id})")
        actual_facultad = actual_facultad.siguiente

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
            print("Datos cargados exitosamente.")

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
