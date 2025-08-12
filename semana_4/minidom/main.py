from xml.dom import minidom

def analizar_universidad_xml(ruta_xml):
	doc = minidom.parse(ruta_xml)
	facultades = doc.getElementsByTagName('facultad')
	print(f"Total de facultades: {len(facultades)}\n")
	for facultad in facultades:
		nombre = facultad.getElementsByTagName('nombre')[0].firstChild.data
		id_facultad = facultad.getAttribute('id')
		carreras = facultad.getElementsByTagName('carrera')
		print(f"Facultad: {nombre} (ID: {id_facultad})")
		print(f"  Carreras:")
		for carrera in carreras:
			print(f"    - {carrera.firstChild.data} (ID: {carrera.getAttribute('id')})")
		personas = facultad.getElementsByTagName('personas')[0]
		profesores = personas.getElementsByTagName('profesor')
		estudiantes = personas.getElementsByTagName('estudiante')
		print(f"  Profesores:")
		for profesor in profesores:
			nombre_prof = profesor.getElementsByTagName('nombre')[0].firstChild.data
			correo_prof = profesor.getElementsByTagName('correo')[0].firstChild.data
			print(f"    - {nombre_prof} (ID: {profesor.getAttribute('id')}), correo: {correo_prof}")
		print(f"  Estudiantes:")
		for estudiante in estudiantes:
			nombre_est = estudiante.getElementsByTagName('nombre')[0].firstChild.data
			correo_est = estudiante.getElementsByTagName('correo')[0].firstChild.data
			edad_est = estudiante.getElementsByTagName('edad')[0].firstChild.data
			print(f"    - {nombre_est} (ID: {estudiante.getAttribute('id')}), correo: {correo_est}, edad: {edad_est}")
		print()


analizar_universidad_xml("C:/Users/Dgo/Documents/IPC2/semana_4/universidad.xml")
