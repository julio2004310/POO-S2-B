class CuentaBancaria:
    """
    Modelo que representa una cuenta bancaria.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        CONSTRUCTOR (__init__)
        Inicializa:
        - Nombre del titular
        - Saldo inicial de la cuenta
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con saldo ${self.saldo}")

    def __del__(self):
        """
        DESTRUCTOR (__del__)
        Se ejecuta cuando el objeto es eliminado.

        Limpieza:
        - Registra que la cuenta dejó de existir
        - Simula cierre de la cuenta
        """
        print(f"Cuenta de {self.titular} cerrada correctamente")
