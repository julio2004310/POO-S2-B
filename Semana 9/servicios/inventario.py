from modelos.producto import Producto


# Clase que gestiona los productos del inventario
class Inventario:

    def __init__(self):
        # Lista donde se almacenan los productos
        self.productos = []

    # Añadir producto
    def añadir_producto(self, id, nombre, cantidad, precio):

        # Validar que el ID no esté repetido
        for producto in self.productos:
            if producto.get_id() == id:
                print("Error: el ID ya existe.")
                return

        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id):

        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado.")
                return

        print("Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):

        for producto in self.productos:

            if producto.get_id() == id:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                print("Producto actualizado.")
                return

        print("Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):

        resultados = []

        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    # Mostrar inventario
    def mostrar_inventario(self):

        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print(producto)