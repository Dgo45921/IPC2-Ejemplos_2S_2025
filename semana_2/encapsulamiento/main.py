from CuentaBanco import CuentaBanco


def main():
    cuenta = CuentaBanco("Fabiano Caruana", 1000)

    # ENCAPSULAMIENTO: Acceso a atributos privados a través de métodos públicos
    print(f"Titular de la cuenta: {cuenta.obtener_titular()}")
    print(f"Saldo inicial: {cuenta.obtener_saldo()}")
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.retirar(1500)  # Intento de retiro mayor al saldo
    print(f"Saldo final: {cuenta.obtener_saldo()}")

    # intento de acceso directo a atributos privados (no recomendado)
    #print(cuenta.__titular) # error
    print(cuenta.edad)  # Acceso al atributo público edad

main()