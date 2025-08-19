import os
from os import system

def graficar_lista(animales):
    dot = 'digraph G {\n'
    dot += '  rankdir = LR;\n'
    dot += '  splines = ortho;\n'
    dot += '  graph [pencolor = transparent, rank = same];\n'
    dot += '  node  [shape = record];\n\n'

    actual = animales.primero
    idx = 1
    dot_nodes = ''
    dot_edges = ''
    primero_name = None
    while actual:
        node_name = f'node{idx}'
        if idx == 1:
            primero_name = node_name
        dot_nodes += f'  {node_name} [label = "{actual.animal.nombre}"]\n'
        if actual.siguiente and actual.siguiente != animales.primero:
            dot_edges += f'  {node_name} -> node{idx+1};\n'
        elif actual.siguiente == animales.primero:
            # Última arista para cerrar el ciclo
            dot_edges += f'  {node_name} -> {primero_name} [constraint=false];\n'
            break
        actual = actual.siguiente
        idx += 1
    dot += dot_nodes + '\n' + dot_edges
    dot += '}'

    # Obtiene la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Define la ruta completa para los archivos de salida
    archivo_dot = os.path.join(directorio_actual, "texto_lista_simple_circular.dot")
    archivo_png = os.path.join(directorio_actual, "grafica_lista_simple_circular.png")

    # Escribe el archivo .dot
    with open(archivo_dot, "w") as nuevo_archivo:
        nuevo_archivo.write(dot)

    # Ejecuta el comando para generar la imagen PNG
    system(f"dot -Tpng {archivo_dot} -o {archivo_png}")
