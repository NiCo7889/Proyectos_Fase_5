import csv # Importamos el módulo csv para poder leer y escribir en ficheros csv
import config # Importamos el módulo config para poder acceder a la variable DATABASE_PATH


class Producto: # Creamos la clase Cliente para poder crear objetos de tipo Cliente con los atributos dni, nombre y apellido
    def __init__(self, CD, nombre, apellido): # Creamos el método __init__ para inicializar los atributos de la clase
        self.CD = CD
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self): # Creamos el método __str__ para poder imprimir los objetos de tipo Cliente
        return f"({self.CD}) {self.nombre} {self.apellido}"

    def to_dict(self): # Creamos el método to_dict para poder convertir los objetos de tipo Cliente en diccionarios
        return {'dni': self.CD, 'nombre': self.nombre, 'apellido': self.apellido}


class Inventario: # Creamos la clase Clientes para poder crear objetos de tipo Clientes con los atributos lista

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for CD, nombre, apellido in reader:
            cliente = Cliente(CD, nombre, apellido)
            lista.append(cliente)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(CD):
        for cliente in Clientes.lista:
            if cliente.CD == CD:
                return cliente

    @staticmethod
    def crear(CD, nombre, apellido):
        cliente = Cliente(CD, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(CD, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.CD == CD:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(CD):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.CD == CD:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.CD, cliente.nombre, cliente.apellido))