class ConexionServidor:
    """
    Clase que simula una conexión a un servidor.
    Sirve para demostrar el uso del constructor y destructor.
    """

    def __init__(self, servidor, puerto):
        """
        CONSTRUCTOR (__init__)
        Se ejecuta al crear el objeto.

        Inicializa:
        - Dirección del servidor
        - Puerto de conexión
        - Estado de la conexión (activa)
        """
        self.servidor = servidor
        self.puerto = puerto
        self.conectado = True
        print(f"Conectado al servidor {self.servidor} en el puerto {self.puerto}")

    def enviar_datos(self, datos):
        """
        Método que simula el envío de datos al servidor.
        """
        if self.conectado:
            print(f"Enviando datos: {datos}")
        else:
            print("No hay conexión activa")

    def __del__(self):
        """
        DESTRUCTOR (__del__)
        Se ejecuta cuando el objeto es eliminado o el programa finaliza.

        Limpieza que realiza:
        - Cierra la conexión simulada
        - Libera el estado del objeto
        """
        if self.conectado:
            self.conectado = False
            print("Conexión cerrada y recursos liberados")


# ---- Uso del programa ----

conexion1 = ConexionServidor("localhost", 8080)
conexion1.enviar_datos("Hola servidor")

# Forzamos la eliminación del objeto
del conexion1

print("Programa finalizado")
