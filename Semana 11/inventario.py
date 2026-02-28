import json
import os
from producto import Producto

# ==========================
# Clase Inventario
# ==========================

class Inventario:
    def __init__(self, archivo="inventario.json"):
        # Diccionario para almacenar productos
        # { id_producto : objeto_producto }
        self.productos = {}
        self.archivo = archivo
        self.cargar_archivo()

    # ===== Añadir producto =====
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠️ El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido correctamente.")
            self.guardar_archivo()

    # ===== Eliminar producto =====
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
            self.guardar_archivo()
        else:
            print("❌ Producto no encontrado.")

    # ===== Actualizar producto =====
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            print("🔄 Producto actualizado.")
            self.guardar_archivo()
        else:
            print("❌ Producto no encontrado.")

    # ===== Buscar por nombre =====
    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            for producto in encontrados:
                self.mostrar_producto(producto)
        else:
            print("❌ No se encontraron productos.")

    # ===== Mostrar producto =====
    def mostrar_producto(self, producto):
        print(f"ID: {producto.get_id()} | "
              f"Nombre: {producto.get_nombre()} | "
              f"Cantidad: {producto.get_cantidad()} | "
              f"Precio: ${producto.get_precio():.2f}")

    # ===== Mostrar todos =====
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    # ===== Guardar en archivo =====
    def guardar_archivo(self):
        datos = {id: prod.to_dict() for id, prod in self.productos.items()}
        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=4)

    # ===== Cargar desde archivo =====
    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for id, prod in datos.items():
                    producto = Producto(
                        prod["id"],
                        prod["nombre"],
                        prod["cantidad"],
                        prod["precio"]
                    )
                    self.productos[id] = producto