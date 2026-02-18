class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    # Convierte el producto en una línea de texto para guardarlo en el archivo
    def to_line(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"
