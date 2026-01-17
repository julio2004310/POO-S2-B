# ==============================
# SERVICIOS - LÓGICA
# ==============================

def mostrar_figura(figura):
    """
    Función que recibe cualquier figura
    Aplica polimorfismo
    """
    figura.mostrar_info()
    print(f"Área: {figura.calcular_area()}")
    print("--------------------------")

