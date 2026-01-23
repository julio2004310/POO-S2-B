from modelos.cuenta_bancaria import CuentaBancaria

class ServicioBancario:
    """
    Servicio que gestiona operaciones bancarias.
    """

    def crear_cuenta(self, titular, saldo_inicial):
        return CuentaBancaria(titular, saldo_inicial)

    def depositar(self, cuenta, monto):
        if monto > 0:
            cuenta.saldo += monto
            print(f"Depósito exitoso. Saldo actual: ${cuenta.saldo}")
        else:
            print("Monto inválido")

    def retirar(self, cuenta, monto):
        if monto <= cuenta.saldo:
            cuenta.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${cuenta.saldo}")
        else:
            print("Fondos insuficientes")
