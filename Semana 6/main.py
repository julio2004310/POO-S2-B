# ==============================
# ARCHIVO PRINCIPAL
# ==============================

from modelos.empleado import EmpleadoTiempoCompleto, EmpleadoMedioTiempo
from servicios.gestor_empleados import mostrar_empleado


def main():
    # Crear instancias de las clases
    empleado1 = EmpleadoTiempoCompleto("Carlos", 1200, 5)
    empleado2 = EmpleadoMedioTiempo("Julio", 600)

    # Usar los servicios
    mostrar_empleado(empleado1)
    mostrar_empleado(empleado2)

    # Demostración de encapsulación
    empleado2.set_salario(700)
    print("Salario actualizado de Julio:", empleado2.get_salario())


# Punto de entrada del programa
if __name__ == "__main__":
    main()
