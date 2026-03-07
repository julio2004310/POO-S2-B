# Modelo que representa un libro dentro del sistema

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        """
        Se utiliza una tupla para almacenar título y autor
        ya que estos datos no deben modificarse después
        de crear el libro (inmutabilidad).
        """
        self._info = (titulo, autor)

        self._categoria = categoria
        self._isbn = isbn

    # Métodos getters para aplicar encapsulamiento
    def obtener_titulo(self):
        return self._info[0]

    def obtener_autor(self):
        return self._info[1]

    def obtener_categoria(self):
        return self._categoria

    def obtener_isbn(self):
        return self._isbn

    def __str__(self):
        return f"Título: {self._info[0]} | Autor: {self._info[1]} | Categoría: {self._categoria} | ISBN: {self._isbn}"