# servicios/inventario.py

from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar los productos.
    Usa una lista como estructura principal de almacenamiento.
    """

    def __init__(self):
        """
        Constructor que inicializa la lista de productos.
        """
        self.productos = []

    # ======================
    # AÑADIR PRODUCTO
    # ======================

    def añadir_producto(self, id_producto, nombre, cantidad, precio):

        # Validar que el ID no esté repetido
        if self.buscar_por_id(id_producto) is not None:
            print("Ya existe un producto con ese ID.")
            return

        nuevo = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo)
        print("Producto añadido correctamente.")

    # ======================
    # ELIMINAR PRODUCTO
    # ======================

    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)

        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # ======================
    # ACTUALIZAR PRODUCTO
    # ======================

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id_producto)

        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # ======================
    # BUSCAR POR ID
    # ======================

    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # ======================
    # BUSCAR POR NOMBRE
    # ======================

    def buscar_por_nombre(self, nombre):
        resultados = []

        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    # ======================
    # MOSTRAR INVENTARIO
    # ======================

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n----- INVENTARIO -----")
        for producto in self.productos:
            print(producto)
