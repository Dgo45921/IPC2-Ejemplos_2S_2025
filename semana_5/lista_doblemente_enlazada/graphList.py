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
    while actual:
        node_name = f'node{idx}'
        dot_nodes += f'  {node_name} [label = "{actual.animal.nombre}"]\n'
        if actual.siguiente:
            dot_edges += f'  {node_name} -> node{idx+1};\n'
            if actual is not animales.primero:
                dot_edges += f'  {node_name} -> node{idx-1};\n'

        actual = actual.siguiente
        idx += 1

    if animales.size > 1:
            dot_nodes += f'  {node_name} [label = "{animales.ultimo.animal.nombre}"]\n' 
            dot_edges += f'  {node_name} -> node{idx-2};\n' 


    dot += dot_nodes + '\n' + dot_edges
    dot += '}'

    # Obtienes la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Define la ruta completa para los archivos de salida
    archivo_dot = os.path.join(directorio_actual, "texto_lista_doble.dot")
    archivo_png = os.path.join(directorio_actual, "grafica_lista_doble.png")

    # Escribe el archivo .dot
    with open(archivo_dot, "w") as nuevo_archivo:
        nuevo_archivo.write(dot)

    # Ejecuta el comando para generar la imagen PNG
    system(f"dot -Tpng {archivo_dot} -o {archivo_png}")
