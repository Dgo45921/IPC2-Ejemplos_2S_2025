from lxml import etree

xml_path = "C:/Users/Dgo/Documents/IPC2/semana_4/universidad.xml"
tree = etree.parse(xml_path)
root = tree.getroot()

# Usar solo XPath para extraer datos
# '//facultad' busca todos los nodos facultad en el documento
facultades = root.xpath('//facultad')
print(f"Total de facultades: {len(facultades)}\n")

for facultad in facultades:
    # 'nombre' hijo directo de facultad
    nombre = facultad.xpath('./nombre/text()')[0]
    id_facultad = facultad.get('id')
    print(f"Facultad: {nombre} (ID: {id_facultad})")

    # './carrera' busca todos los hijos carrera de la facultad actual
    carreras = facultad.xpath('./carrera')
    print("  Carreras:")
    for carrera in carreras:
        print(f"    - {carrera.text} (ID: {carrera.get('id')})")

    # './personas/profesor' busca todos los profesores dentro de personas de la facultad
    profesores = facultad.xpath('./personas/profesor')
    print("  Profesores:")
    for profesor in profesores:
        nombre_prof = profesor.xpath('./nombre/text()')[0]
        correo_prof = profesor.xpath('./correo/text()')[0]
        id_prof = profesor.get('id')
        print(f"    - {nombre_prof} (ID: {id_prof}), correo: {correo_prof}")

    # './personas/estudiante' busca todos los estudiantes dentro de personas de la facultad
    estudiantes = facultad.xpath('./personas/estudiante')
    print("  Estudiantes:")
    for estudiante in estudiantes:
        nombre_est = estudiante.xpath('./nombre/text()')[0]
        correo_est = estudiante.xpath('./correo/text()')[0]
        edad_est = estudiante.xpath('./edad/text()')[0]
        id_est = estudiante.get('id')
        print(f"    - {nombre_est} (ID: {id_est}), correo: {correo_est}, edad: {edad_est}")
    print()

# Ejemplo de XPath usando atributos (@) y condiciones:
# Buscar todas las carreras con id='1' en cualquier facultad
carreras_id1 = root.xpath('//carrera[@id="1"]')
print("Carreras con id=1:")
for carrera in carreras_id1:
    print(f"  - {carrera.text}")

# Buscar todos los estudiantes mayores de 22 años usando XPath condicional
estudiantes_mayores_22 = root.xpath('//estudiante[number(edad)>22]')
print("Estudiantes mayores de 22 años:")
for est in estudiantes_mayores_22:
    print(f"  - {est.xpath('./nombre/text()')[0]} (Edad: {est.xpath('./edad/text()')[0]})")