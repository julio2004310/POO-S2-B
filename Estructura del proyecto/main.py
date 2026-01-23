from servicios.servicio_bancario import ServicioBancario

def main():
    servicio = ServicioBancario()

    cuenta1 = servicio.crear_cuenta("Julio Quiñonez", 500)
    servicio.depositar(cuenta1, 200)
    servicio.retirar(cuenta1, 100)

    # Eliminamos el objeto para evidenciar el destructor
    del cuenta1

    print("Fin del programa")

if __name__ == "__main__":
    main()
