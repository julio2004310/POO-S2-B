import os
from servicios.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ==============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==============================
    def cargar_desde_archivo(self):
        try:
            # Si el archivo no existe, lo creamos
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")

                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        producto = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        self.productos.append(producto)

        except FileNotFoundError:
            print("El archivo no fue encontrado. Se creará uno nuevo.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except ValueError:
            print("El archivo contiene datos corruptos.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    # ==============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ==============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_line())

            print("Inventario guardado correctamente.")

        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # ==============================
    # AÑADIR PRODUCTO
    # ==============================
    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                print("El producto ya existe.")
                return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("Producto añadido exitosamente.")

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    # ==============================
    # ACTUALIZAR PRODUCTO
    # ==============================
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:

                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad

                if nuevo_precio is not None:
                    producto.precio = nuevo_precio

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    # ==============================
    # BUSCAR POR NOMBRE
    # ==============================
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    # ==============================
    # MOSTRAR INVENTARIO
    # ==============================
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)
