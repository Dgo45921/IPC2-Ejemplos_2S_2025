# main.py

# del modulo Persona importa clase Persona
from Persona import Persona

def main():
    # Creando instancias de la clase Persona
    persona1 = Persona("Diego", 23)
    persona2 = Persona("Juana", 25, True)


    # Llamar al método saludar
    print(persona1.saludar())
    print(persona2.saludar())

    # Preguntar si están casados
    print(persona1.decir_si_estoy_casado())
    print(persona2.decir_si_estoy_casado())

main()

