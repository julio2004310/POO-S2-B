import os
import subprocess

# --------------------------------------------------
# Función que muestra el contenido de un script Python
# --------------------------------------------------
def mostrar_codigo(ruta_script):
    try:
        # Abrimos el archivo en modo lectura
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()

            # Mostramos el código por pantalla
            print("\n--- CÓDIGO DEL SCRIPT ---\n")
            print(codigo)

            # Retornamos True indicando que se pudo leer
            return True
    except FileNotFoundError:
        print("❌ El archivo no existe.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")

    # Si ocurre algún error, retornamos False
    return False


# --------------------------------------------------
# Función que ejecuta un script Python en otra consola
# --------------------------------------------------
def ejecutar_codigo(ruta_script):
    try:
        # Si el sistema operativo es Windows
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        # Para sistemas Linux o macOS
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"❌ Error al ejecutar el script: {e}")


# --------------------------------------------------
# Menú principal del programa
# --------------------------------------------------
def mostrar_menu():
    # Ruta donde se encuentra este archivo (dashboard.py)
    ruta_base = os.path.dirname(__file__)

    while True:
        print("\n=== MENÚ PRINCIPAL ==")
        print("1 - Unidad 1")
        print("2 - Unidad 2")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        # Salir del programa
        if opcion == '0':
            print("Programa finalizado.")
            break

        # Construimos la ruta de la unidad seleccionada
        ruta_unidad = os.path.join(ruta_base, f"Unidad {opcion}")

        # Verificamos si la unidad existe
        if os.path.exists(ruta_unidad):
            mostrar_sub_menu(ruta_unidad)
        else:
            print("❌ La unidad no existe.")


# --------------------------------------------------
# Submenú que muestra las subcarpetas de una unidad
# --------------------------------------------------
def mostrar_sub_menu(ruta_unidad):
    # Listamos solo las carpetas
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    # Si no hay subcarpetas, regresamos
    if not sub_carpetas:
        print("❌ No hay subcarpetas.")
        return

    while True:
        print("\n--- SUBMENÚ ---")
        for i, carpeta in enumerate(sub_carpetas, 1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar")

        opcion = input("Seleccione una opción: ")

        # Regresar al menú principal
        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(sub_carpetas):
                ruta_sub = os.path.join(ruta_unidad, sub_carpetas[indice])
                mostrar_scripts(ruta_sub)
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


# --------------------------------------------------
# Menú que muestra los scripts Python disponibles
# --------------------------------------------------
def mostrar_scripts(ruta_sub_carpeta):
    # Listamos solo archivos .py
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ]

    # Si no hay scripts, regresamos
    if not scripts:
        print("❌ No hay scripts en esta carpeta.")
        return

    while True:
        print("\n--- SCRIPTS DISPONIBLES ---")
        for i, script in enumerate(scripts, 1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        opcion = input("Seleccione un script: ")

        # Regresar al submenú
        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])

                # Mostramos el código del script
                if mostrar_codigo(ruta_script):
                    ejecutar = input("¿Desea ejecutar el script? (1 = Sí / 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)

                    input("\nPresione Enter para continuar...")
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


# --------------------------------------------------
# Punto de entrada del programa
# --------------------------------------------------
if __name__ == "__main__":
    mostrar_menu()
