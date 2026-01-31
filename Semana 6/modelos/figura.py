# =============================
# MODELOS - FIGURAS GEOMÉTRICAS
# =============================

class Figura:
    """
    Clase base Figura
    Aplica herencia y polimorfismo
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area(self):
        # Método que será sobrescrito
        pass

    def mostrar_info(self):
        print(f"Figura: {self.nombre}")


class Cuadrado(Figura):
    """
    Clase derivada Cuadrado
    Aplica encapsulación
    """

    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado  # Atributo privado (encapsulación)

    def calcular_area(self):
        return self.__lado ** 2


class Rectangulo(Figura):
    """
    Clase derivada Rectángulo
    """

    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):
    """
    Clase derivada Círculo
    """

    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2
