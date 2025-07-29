from abc import ABC, abstractmethod

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
