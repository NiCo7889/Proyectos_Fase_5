import os 
import helpers
import database as db # importo database como db para poder usar sus funciones


def iniciar(): # Función que inicia el programa y muestra el menú
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Inventario  ")
        print("========================")
        print("[1] Listar los productos ")
        print("[2] Buscar un producto   ")
        print("[3] Añadir un producto   ")
        print("[4] Modificar un producto  ")
        print("[5] Borrar un producto   ")
        print("[6] Cerrar el inventario    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        elif opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo un cliente...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '4':
            print("Modificando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            print("Borrando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(
                dni) else print("Cliente no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
        
        elif opcion != '1, 2, 3, 4, 5, 6':
            print("Opción incorrecta. Introduce una opción válida.\n")

        input("\nPresiona ENTER para continuar...")