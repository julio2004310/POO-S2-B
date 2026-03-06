#main
from servicios.inventario import Inventario


def menu():

    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")


def main():

    inventario = Inventario()

    while True:

        menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            try:

                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                inventario.añadir_producto(id_producto, nombre, cantidad, precio)

            except ValueError:
                print("Datos inválidos.")

        elif opcion == "2":

            id_producto = input("ID del producto: ")

            inventario.eliminar_producto(id_producto)

        elif opcion == "3":

            id_producto = input("ID del producto: ")

            try:

                cantidad = input("Nueva cantidad (Enter para no cambiar): ")
                precio = input("Nuevo precio (Enter para no cambiar): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Datos inválidos.")

        elif opcion == "4":

            nombre = input("Nombre a buscar: ")

            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:

                for p in resultados:
                    print(p)

            else:
                print("No encontrado.")

        elif opcion == "5":

            inventario.mostrar_inventario()

        elif opcion == "6":

            print("Saliendo...")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    main()