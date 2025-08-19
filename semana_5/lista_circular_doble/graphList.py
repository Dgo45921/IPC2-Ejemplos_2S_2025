import os
from os import system

def graficar_lista(animales):
    dot = 'digraph G {\n'
    dot += '  rankdir = LR;\n'
    dot += '  splines = ortho;\n'
    dot += '  graph [pencolor = transparent, rank = same];\n'
    dot += '  node  [shape = record];\n\n'

    actual = animales.primero
    dot_nodes = ''
    dot_edges = ''
    # Si la lista está vacía, no graficar nada
    if not actual:
        dot += '}'
    else:
        # Primer recorrido: crear nodos
        primero = animales.primero
        n = animales.size
        temp = primero
        for i in range(n):
            node_name = f'node{i+1}'
            dot_nodes += f'  {node_name} [label = "{temp.animal.nombre}"]\n'
            temp = temp.siguiente
        # Segundo recorrido: crear aristas siguiente y anterior
        temp = primero
        for i in range(n):
            node_name = f'node{i+1}'
            next_name = f'node{((i+1)%n)+1}'
            prev_name = f'node{((i-1+n)%n)+1}'
            if i == n-1:
                dot_edges += f'  {node_name} -> {next_name}[constraint = false];\n'
                dot_edges += f'  {node_name} -> {prev_name} ;\n'
            else:
                dot_edges += f'  {node_name} -> {next_name};\n'
                dot_edges += f'  {node_name} -> {prev_name};\n'


            temp = temp.siguiente


        dot += dot_nodes + '\n' + dot_edges
        dot += '}'

    # Obtiene la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # Define la ruta completa para los archivos de salida
    archivo_dot = os.path.join(directorio_actual, "texto_lista_doble.dot")
    archivo_png = os.path.join(directorio_actual, "grafica_lista_doble.png")

    # Escribe el archivo .dot
    with open(archivo_dot, "w") as nuevo_archivo:
        nuevo_archivo.write(dot)

    # Ejecuta el comando para generar la imagen PNG
    system(f"dot -Tpng {archivo_dot} -o {archivo_png}")
