from abc import ABC, abstractmethod

# Abstracción: Clase base Animal
class Animal(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamiento
        self.__edad = edad      # Encapsulamiento

    
    def get_nombre(self):
        return self.__nombre

    
    def get_edad(self):
        return self.__edad

    @abstractmethod
    def sonido(self):
        pass

    @abstractmethod
    def costo_mantenimiento(self):
        pass
