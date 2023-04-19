import csv # Importamos el módulo csv para poder leer y escribir en ficheros csv
import config # Importamos el módulo config para poder acceder a la variable DATABASE_PATH


class Producto: # Creamos la clase Cliente para poder crear objetos de tipo Cliente con los atributos dni, nombre y apellido
    def __init__(self, CD, Producto, categoria): # Creamos el método __init__ para inicializar los atributos de la clase
        self.CD = CD
        self.Producto = Producto
        self.apellido = apellido

    def __str__(self): # Creamos el método __str__ para poder imprimir los objetos de tipo Cliente
        return f"({self.CD}) {self.Producto} {self.apellido}"

    def to_dict(self): # Creamos el método to_dict para poder convertir los objetos de tipo Cliente en diccionarios
        return {'dni': self.CD, 'nombre': self.Producto, 'apellido': self.apellido}


class Inventario: # Creamos la clase Clientes para poder crear objetos de tipo Clientes con los atributos lista

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for CD, Producto, apellido in reader:
            cliente = Cliente(CD, nombre, apellido)
            lista.append(cliente)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(CD):
        for cliente in Inventario.lista:
            if cliente.CD == CD:
                return cliente

    @staticmethod
    def crear(CD, Producto, apellido):
        cliente = Cliente(CD, Producto, apellido)
        Inventario.lista.append(cliente)
        Inventario.guardar()
        return cliente

    @staticmethod
    def modificar(CD, Producto, apellido):
        for indice, cliente in enumerate(Inventario.lista):
            if cliente.CD == CD:
                Inventario.lista[indice].Producto = Producto
                Inventario.lista[indice].apellido = apellido
                Inventario.guardar()
                return Inventario.lista[indice]

    @staticmethod
    def borrar(CD):
        for indice, cliente in enumerate(Inventario.lista):
            if cliente.CD == CD:
                cliente = Inventario.lista.pop(indice)
                Inventario.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Inventario.lista:
                writer.writerow((cliente.CD, cliente.Producto, cliente.apellido))