import csv # Importamos el módulo csv para poder leer y escribir en ficheros csv
import config # Importamos el módulo config para poder acceder a la variable DATABASE_PATH


class Producto: # Creamos la clase Cliente para poder crear objetos de tipo Producto con los atributos dni, nombre y apellido
    def __init__(self, CD, Producto, categoria): # Creamos el método __init__ para inicializar los atributos de la clase
        self.CD = CD
        self.Producto = Producto
        self.categoria = categoria

    def __str__(self): # Creamos el método __str__ para poder imprimir los objetos de tipo Producto
        return f"({self.CD}) {self.Producto} {self.categoria}"

    def to_dict(self): # Creamos el método to_dict para poder convertir los objetos de tipo Producto en diccionarios
        return {'CD': self.CD, 'Producto': self.Producto, 'apellido': self.categoria}


class Inventario: # Creamos la clase Clientes para poder crear objetos de tipo Clientes con los atributos lista

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for CD, Producto, categoria in reader:
            Producto = Producto(CD, Producto, categoria)
            lista.append(Producto)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(CD):
        for Producto in Inventario.lista:
            if Producto.CD == CD:
                return Producto

    @staticmethod
    def crear(CD, Producto, categoria):
        Producto = Producto(CD, Producto, categoria)
        Inventario.lista.append(Producto)
        Inventario.guardar()
        return Producto

    @staticmethod
    def modificar(CD, Producto, categoria):
        for indice, cliente in enumerate(Inventario.lista):
            if cliente.CD == CD:
                Inventario.lista[indice].Producto = Producto
                Inventario.lista[indice].categoria = categoria
                Inventario.guardar()
                return Inventario.lista[indice]

    @staticmethod
    def borrar(CD):
        for indice, Producto in enumerate(Inventario.lista):
            if Producto.CD == CD:
                Producto = Inventario.lista.pop(indice)
                Inventario.guardar()
                return Producto

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for Producto in Inventario.lista:
                writer.writerow((Producto.CD, Producto.Producto, Producto.categoria))