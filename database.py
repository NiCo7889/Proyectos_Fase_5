import csv # Importamos el módulo csv para poder leer y escribir en ficheros csv
import config # Importamos el módulo config para poder acceder a la variable DATABASE_PATH


class Producto: # Creamos la clase Cliente para poder crear objetos de tipo Producto con los atributos dni, nombre y apellido
    def __init__(self, CD, producto, categoria): # Creamos el método __init__ para inicializar los atributos de la clase
        self.CD = CD
        self.producto = producto
        self.categoria = categoria

    def __str__(self): # Creamos el método __str__ para poder imprimir los objetos de tipo Producto
        return f"({self.CD}) {self.producto} {self.categoria}"

    def to_dict(self): # Creamos el método to_dict para poder convertir los objetos de tipo Producto en diccionarios
        return {'CD': self.CD, 'Producto': self.producto, 'apellido': self.categoria}


class Inventario: # Creamos la clase Clientes para poder crear objetos de tipo Clientes con los atributos lista

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for CD, producto, categoria in reader:
            Producto1 = Producto(CD, producto, categoria)
            lista.append(Producto1)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(CD):
        for producto in Inventario.lista:
            if producto.CD == CD:
                return producto

    @staticmethod
    def crear(CD, producto, categoria):
        producto = Producto(CD, producto, categoria)
        Inventario.lista.append(producto)
        Inventario.guardar()
        return producto

    @staticmethod
    def modificar(CD, producto, categoria):
        for indice, cliente in enumerate(Inventario.lista):
            if cliente.CD == CD:
                Inventario.lista[indice].producto = producto
                Inventario.lista[indice].categoria = categoria
                Inventario.guardar()
                return Inventario.lista[indice]

    @staticmethod
    def borrar(CD):
        for indice, producto in enumerate(Inventario.lista):
            if producto.CD == CD:
                producto = Inventario.lista.pop(indice)
                Inventario.guardar()
                return producto

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for producto in Inventario.lista:
                writer.writerow((producto.CD, producto.producto, producto.categoria))