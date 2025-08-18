from TDA.NodoFacultad import NodoFacultad

class ListaFacultad:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def insertar(self, facultad):
        nuevo_nodo = NodoFacultad(facultad)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.size += 1
    
    def __str__(self):
        resultado = []
        actual = self.primero
        while actual is not None:
            facultad = actual.facultad
            facultad_str = f"Facultad: {facultad.id} - {facultad.nombre}"
            alumnos_str = ""
            if hasattr(facultad, 'alumnos') and facultad.alumnos is not None:
                alumnos_str = "Alumnos:\n" + str(facultad.alumnos)
            resultado.append(facultad_str + ("\n" + alumnos_str if alumnos_str else ""))
            actual = actual.siguiente
        return "\n\n".join(resultado)
