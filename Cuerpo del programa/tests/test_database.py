import csv
import copy
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.Inventario.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Inventario.buscar('15J')
        cliente_inexistente = db.Inventario.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Inventario.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Inventario.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.Producto, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Inventario.buscar('28Z'))
        cliente_modificado = db.Inventario.modificar('28Z', 'Mariana', 'García')
        self.assertEqual(cliente_a_modificar.Producto, 'Ana')
        self.assertEqual(cliente_modificado.Producto, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Inventario.borrar('48H')
        cliente_rebuscado = db.Inventario.buscar('48H')
        self.assertEqual(cliente_borrado.dni, '48H')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Inventario.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Inventario.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Inventario.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Inventario.lista))

    def test_escritura_csv(self):
        db.Inventario.borrar('48H')
        db.Inventario.borrar('15J')
        db.Inventario.modificar('28Z', 'Mariana', 'García')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, Producto, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(Producto, 'Mariana')
        self.assertEqual(apellido, 'García')


if __name__ == '__main__':
    unittest.main()