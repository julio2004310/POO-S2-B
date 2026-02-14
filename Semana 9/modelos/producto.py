# modelos/producto.py

class Producto:
    """
    Clase que representa un producto del inventario.
    Aplica encapsulamiento usando atributos privados.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor que inicializa los atributos del producto.
        """
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ======================
    # GETTERS
    # ======================

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # =====================
    # SETTERS
    # =====================

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def __str__(self):
        """
        Método especial para mostrar el producto de forma legible.
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
