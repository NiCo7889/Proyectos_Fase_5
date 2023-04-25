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
            print("Listando los productos...\n")
            for Producto in db.Inventario.lista:
                print(Producto)

        elif opcion == '2':
            print("Buscando un producto...\n")
            CD = helpers.leer_texto(3, 3, "CD (2 int y 1 char)").upper()
            Producto = db.Inventario.buscar(CD)
            print(Producto) if Producto else print("Producto no encontrado.")

        elif opcion == '3':
            print("Añadiendo un producto...\n")

            CD = None
            while True:
                CD = helpers.leer_texto(3, 3, "CD (2 int y 1 char)").upper()
                if helpers.CD_valido(CD, db.Inventario.lista):
                    break

            Producto = helpers.leer_texto(2, 30, "Producto (de 2 a 30 chars)").capitalize()
            categoria = helpers.leer_texto(2, 30, "categoria (de 2 a 30 chars)").capitalize()
            db.Inventario.crear(CD, Producto, categoria)
            print("Producto añadido correctamente.")

        elif opcion == '4':
            print("Modificando un Producto...\n")
            CD = helpers.leer_texto(3, 3, "CD (2 int y 1 char)").upper()
            Producto = db.Inventario.buscar(CD)
            if Producto:
                Producto = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{Producto.Producto}]").capitalize()
                categoria = helpers.leer_texto(
                    2, 30, f"categoria (de 2 a 30 chars) [{Producto.categoria}]").capitalize()
                db.Inventario.modificar(Producto.CD, Producto, categoria)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            print("Borrando un producto...\n")
            CD = helpers.leer_texto(3, 3, "CD (2 int y 1 char)").upper()
            print("Producto borrado correctamente.") if db.Inventario.borrar(
                CD) else print("Producto no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
        
        elif opcion != '1, 2, 3, 4, 5, 6':
            print("Opción incorrecta. Introduce una opción válida.\n")

        input("\nPresiona ENTER para continuar...")