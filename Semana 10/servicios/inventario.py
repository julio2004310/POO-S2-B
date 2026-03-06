import os
from servicios.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = []
        self.archivo = "inventario.txt"
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):

        try:

            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r") as file:

                for linea in file:

                    datos = linea.strip().split(",")

                    if len(datos) == 4:

                        id_producto = datos[0]
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id_producto, nombre, cantidad, precio)

                        self.productos.append(producto)

        except Exception as e:
            print("Error al cargar archivo:", e)

    def guardar_en_archivo(self):

        try:

            with open(self.archivo, "w") as file:

                for producto in self.productos:

                    file.write(producto.to_line())

        except Exception as e:
            print("Error al guardar archivo:", e)

    def añadir_producto(self, id_producto, nombre, cantidad, precio):

        for producto in self.productos:

            if producto.id_producto == id_producto:
                print("El producto ya existe.")
                return

        nuevo = Producto(id_producto, nombre, cantidad, precio)

        self.productos.append(nuevo)

        self.guardar_en_archivo()

        print("Producto añadido.")

    def eliminar_producto(self, id_producto):

        for producto in self.productos:

            if producto.id_producto == id_producto:

                self.productos.remove(producto)

                self.guardar_en_archivo()

                print("Producto eliminado.")

                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):

        for producto in self.productos:

            if producto.id_producto == id_producto:

                if cantidad is not None:
                    producto.cantidad = cantidad

                if precio is not None:
                    producto.precio = precio

                self.guardar_en_archivo()

                print("Producto actualizado.")

                return

        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):

        resultados = []

        for producto in self.productos:

            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)

        return resultados

    def mostrar_inventario(self):

        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos:
            print(producto)