# =============================
# ARCHIVO PRINCIPAL
# PROGRAMA POO - FIGURAS GEOMÉTRICAS
# =============================

# -------- CLASE BASE --------
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


# -------- CLASE DERIVADA --------
class Cuadrado(Figura):
    """
    Clase Cuadrado
    Aplica encapsulación
    """

    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado  # Atributo privado (encapsulación)

    def calcular_area(self):
        return self.__lado ** 2


# -------- CLASE DERIVADA --------
class Rectangulo(Figura):
    """
    Clase Rectángulo
    """

    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# -------- CLASE DERIVADA --------
class Circulo(Figura):
    """
    Clase Círculo
    """

    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================
def main():
    # Crear instancias de las clases
    cuadrado = Cuadrado(4)
    rectangulo = Rectangulo(5, 3)
    circulo = Circulo(2)

    # Lista de figuras (polimorfismo)
    figuras = [cuadrado, rectangulo, circulo]

    for figura in figuras:
        figura.mostrar_info()
        print(f"Área: {figura.calcular_area()}")
        print("--------------------------")


# ==============================
# EJECUCIÓN DEL PROGRAMA
# ==============================
if __name__ == "__main__":
    main()

