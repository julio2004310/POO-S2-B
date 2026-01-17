# Programa principal que convierte temperaturas y muestra datos del usuario

from modelos.usuario import Usuario
from servicios.conversor_temperatura import celsius_a_fahrenheit

nombre_usuario = input("Ingrese su nombre: ")
edad_usuario = int(input("Ingrese su edad: "))
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))

usuario = Usuario(nombre_usuario, edad_usuario)
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

print("\nResultados")
print("Nombre:", usuario.nombre)
print("Edad:", usuario.edad)
print("Es mayor de edad:", usuario.es_mayor_de_edad())
print("Temperatura en Fahrenheit:", temperatura_fahrenheit)
