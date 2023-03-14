import csv # Importamos el módulo csv para poder leer y escribir en ficheros csv
import config # Importamos el módulo config para poder acceder a la variable DATABASE_PATH


class Cliente: # Creamos la clase Cliente para poder crear objetos de tipo Cliente con los atributos dni, nombre y apellido
    def __init__(self, dni, nombre, apellido): # Creamos el método __init__ para inicializar los atributos de la clase
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self): # Creamos el método __str__ para poder imprimir los objetos de tipo Cliente
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self): # Creamos el método to_dict para poder convertir los objetos de tipo Cliente en diccionarios
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}


class Clientes: # Creamos la clase Clientes para poder crear objetos de tipo Clientes con los atributos lista

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))