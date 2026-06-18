class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo: ")

        contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(contacto)

        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No existen contactos registrados.")
        else:
            print("\nLISTA DE CONTACTOS")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                print("---------------------")

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre a buscar: ")

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                return

        print("Contacto no encontrado.")

    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a eliminar: ")

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print("Contacto eliminado correctamente.")
                return

        print("Contacto no encontrado.")

agenda = Agenda()

while True:
    print("\nAGENDA TELEFÓNICA")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agenda.agregar_contacto()
    elif opcion == "2":
        agenda.mostrar_contactos()
    elif opcion == "3":
        agenda.buscar_contacto()
    elif opcion == "4":
        agenda.eliminar_contacto()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")
