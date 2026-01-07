# ==============================
# MODELOS - CLASES
# ==============================

class Empleado:
    """
    Clase base Empleado
    Aplica encapsulación, herencia y polimorfismo
    """

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # Encapsulación

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario

    def calcular_bono(self):
        # Método que será sobrescrito (polimorfismo)
        return self.__salario * 0.10

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario: ${self.__salario}")


class EmpleadoTiempoCompleto(Empleado):
    """
    Clase derivada (herencia)
    """

    def __init__(self, nombre, salario, antiguedad):
        super().__init__(nombre, salario)
        self.antiguedad = antiguedad

    # Polimorfismo
    def calcular_bono(self):
        return self.get_salario() * 0.20 + (self.antiguedad * 50)


class EmpleadoMedioTiempo(Empleado):
    """
    Clase derivada (herencia)
    """

    # Polimorfismo
    def calcular_bono(self):
        return self.get_salario() * 0.05
