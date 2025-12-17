class Producto:
    def __init__(self, nombre, precio, stock):
        # Abstracción: Definición de atributos esenciales del objeto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_inventario(self, cantidad):
        # Método que valida y modifica el estado interno del stock (Comportamiento)
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

class Carrito:
    def __init__(self):
        # El carrito gestiona una colección de objetos de la clase Producto
        self.productos_seleccionados = []

    def agregar_item(self, producto, cantidad):
        # Interacción entre objetos: El carrito solicita una acción al objeto Producto
        if producto.actualizar_inventario(cantidad):
            self.productos_seleccionados.append({'obj': producto, 'cant': cantidad})
            print(f"Confirmación: {producto.nombre} añadido.")
        else:
            print(f"Aviso: Stock insuficiente para {producto.nombre}.")

    def obtener_total(self):
        # Método para calcular el costo acumulado de los objetos contenidos
        total = 0
        for item in self.productos_seleccionados:
            total += item['obj'].precio * item['cant']
        return total