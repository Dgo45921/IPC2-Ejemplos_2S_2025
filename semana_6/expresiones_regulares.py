# expresiones_regulares.py
import re

def expresiones():
    texto = "El precio es 45.50 USD y el código es ABC123"

    m = re.search(r"\d+\.\d+", texto)
    # m = re.search(r"(\d+)\.(\d+)", texto)
    
    print("Precio encontrado:", m.group()) # todo el match
    print("Parte entera:", m.group(0)) # primer grupo
    print("Índice inicio:", m.start())
    print("Índice fin:", m.end())

    # print(m.group(1)) # 45
    # print(m.group(2)) # 50

    numeros = re.findall(r"\d+", texto)
    print("Todos los números:", numeros)

    nuevo_texto = re.sub(r"USD", "Q", texto)
    print("Texto modificado:", nuevo_texto)

    # Buscar todas las palabras en mayúsculas
    mayusculas = re.findall(r"\b[A-Z]+\b", texto)
    print("Palabras en mayúsculas:", mayusculas)

    # Extraer códigos alfanuméricos de 3 letras seguidas de 3 dígitos
    codigos = re.findall(r"\b[A-Z]{3}\d{3}\b", texto)
    print("Códigos encontrados:", codigos)

    # Verificar si cadenas son completamente numéricas
    cadenas = ["12345", "abc123", "7890", "00a11"]
    for c in cadenas:
        es_numerica = bool(re.fullmatch(r"\d+", c))
        print(f"{c} es numérica?:", es_numerica)

def main():
    expresiones()
main()
