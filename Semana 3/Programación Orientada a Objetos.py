class ClimaSemanal:
    # Encapsulamiento de los datos
    def __init__(self):
        self.__temps = []

    def ingresar(self):
        for i in range(7):
            self.__temps.append(float(input(f"Temperatura día {i+1}: ")))

    # Polimorfismo: método que puede sobrescribirse si se heredara
    def promedio(self):
        return round(sum(self.__temps) / len(self.__temps), 2)

    def mostrar(self):
        print("\nPromedio semanal:", self.promedio(), "°C")

# Programa principal
if __name__ == "__main__":
    clima = ClimaSemanal()
    clima.ingresar()
    clima.mostrar()
