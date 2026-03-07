# Clase que contiene la lógica del sistema
# Aquí se gestionan libros, usuarios, préstamos y búsquedas

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario para almacenar libros disponibles
        # Clave = ISBN
        # Valor = objeto Libro
        self._libros = {}

        # Diccionario para usuarios registrados
        self._usuarios = {}

        # Set para asegurar IDs únicos
        self._ids_usuarios = set()

    # ---------------- LIBROS ----------------

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self._libros:
            print("El libro ya existe en el sistema.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self._libros[isbn] = libro

        print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self._libros:
            del self._libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self._ids_usuarios:
            print("El ID de usuario ya está registrado.")
            return

        usuario = Usuario(nombre, id_usuario)

        self._usuarios[id_usuario] = usuario
        self._ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):

        if id_usuario in self._usuarios:

            del self._usuarios[id_usuario]
            self._ids_usuarios.remove(id_usuario)

            print("Usuario eliminado del sistema.")
        else:
            print("Usuario no encontrado.")

    # ---------------- PRESTAMOS ----------------

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self._usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self._libros:
            print("Libro no disponible.")
            return

        usuario = self._usuarios[id_usuario]
        libro = self._libros.pop(isbn)

        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self._usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self._usuarios[id_usuario]

        for libro in usuario.obtener_libros():

            if libro.obtener_isbn() == isbn:

                usuario.devolver_libro(libro)
                self._libros[isbn] = libro

                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # ---------------- BUSQUEDAS ----------------

    def buscar_por_titulo(self, titulo):

        for libro in self._libros.values():

            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self._libros.values():

            if libro.obtener_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self._libros.values():

            if libro.obtener_categoria().lower() == categoria.lower():
                print(libro)

    # ---------------- LISTAR LIBROS DE USUARIO ----------------

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self._usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self._usuarios[id_usuario]

        libros = usuario.obtener_libros()

        if not libros:
            print("El usuario no tiene libros prestados.")
            return

        for libro in libros:
            print(libro)