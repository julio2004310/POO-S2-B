# ---------------------------------------------
# Programa: Promedio Semanal de Temperaturas
# Enfoque: Programación Tradicional
# ---------------------------------------------

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("=== Ingreso de Temperaturas Diarias ===")
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print("\nEl promedio semanal de temperaturas es:", round(promedio, 2), "°C")

# Llamada al programa
if __name__ == "__main__":
    main()
