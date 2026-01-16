"""
Programa para calcular el área de un rectángulo.
Solicita al usuario el ancho y el alto, valida los datos
y muestra el área calculada.
"""

def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.
    :param ancho: ancho del rectángulo (float)
    :param alto: alto del rectángulo (float)
    :return: área del rectángulo (float)
    """
    return ancho * alto


# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")  # string
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))  # float
alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))  # float

# Validar si los valores son positivos
datos_validos = ancho_rectangulo > 0 and alto_rectangulo > 0  # boolean

if datos_validos:
    area = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
    print(f"\nHola {nombre_usuario}, el área del rectángulo es: {area}")
else:
    print("\nError: El ancho y el alto deben ser mayores que cero.")


