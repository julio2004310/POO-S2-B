class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0   # atributo encapsulado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def obtener_saldo(self):
        return self.__saldo
