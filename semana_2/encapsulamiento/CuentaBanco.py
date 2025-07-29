class CuentaBanco:
    def __init__(self, titular, saldo=0, edad=18):
        self.__titular = titular
        self.__saldo = saldo
        self.edad = edad  # Atributo público para la edad, no encapsulado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a retirar debe ser positiva y no puede exceder el saldo actual.")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular