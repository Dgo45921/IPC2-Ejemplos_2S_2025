from Barco import Barco
from Carro import Carro

def main():
    # Crear un objeto Barco
    barco = Barco("Marítimo", "Yamaha", "Blanco", 150)
    print(f"Barco: {barco.obtener_medio()}, Marca: {barco.obtener_marca()}, Color: {barco.obtener_color()}, Millas Náuticas Recorridas: {barco.obtener_millas_nauticas_recorridas()}")

    # Crear un objeto Carro
    carro = Carro("Terrestre", "Toyota", "Rojo", 4)
    print(f"Carro: {carro.obtener_medio()}, Marca: {carro.obtener_marca()}, Color: {carro.obtener_color()}, Ruedas: {carro.obtener_ruedas()}")

main()
