# ==============================
# SERVICIOS - LÓGICA DEL SISTEMA
# ==============================

def mostrar_empleado(empleado):
    """
    Función que trabaja con cualquier tipo de empleado
    Aplica polimorfismo
    """
    empleado.mostrar_info()
    print(f"Bono: ${empleado.calcular_bono()}")
    print("----------------------------")
