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
            db.Producto('15J', 'Marta', 'Pérez'),
            db.Producto('48H', 'Manolo', 'López'),
            db.Producto('28Z', 'Ana', 'García')
        ]

    def test_buscar_Producto(self):
        Producto_existente = db.Inventario.buscar('15J')
        Producto_inexistente = db.Inventario.buscar('99X')
        self.assertIsNotNone(Producto_existente)
        self.assertIsNone(Producto_inexistente)

    def test_crear_Producto(self):
        nuevo_Producto = db.Inventario.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Inventario.lista), 4)
        self.assertEqual(nuevo_Producto.CD, '39X')
        self.assertEqual(nuevo_Producto.Producto, 'Héctor')
        self.assertEqual(nuevo_Producto.categoria, 'Costa')

    def test_modificar_Producto(self):
        Producto_a_modificar = copy.copy(db.Inventario.buscar('28Z'))
        Producto_modificado = db.Inventario.modificar('28Z', 'Mariana', 'García')
        self.assertEqual(Producto_a_modificar.Producto, 'Ana')
        self.assertEqual(Producto_modificado.Producto, 'Mariana')

    def test_borrar_Producto(self):
        cliente_borrado = db.Inventario.borrar('48H')
        cliente_rebuscado = db.Inventario.buscar('48H')
        self.assertEqual(cliente_borrado.CD, '48H')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.CD_valido('00A', db.Inventario.lista))
        self.assertFalse(helpers.CD_valido('232323S', db.Inventario.lista))
        self.assertFalse(helpers.CD_valido('F35', db.Inventario.lista))
        self.assertFalse(helpers.CD_valido('48H', db.Inventario.lista))

    def test_escritura_csv(self):
        db.Inventario.borrar('48H')
        db.Inventario.borrar('15J')
        db.Inventario.modificar('28Z', 'Mariana', 'García')

        CD, Producto, categoria = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            CD, Producto, categoria = next(reader)

        self.assertEqual(CD, '28Z')
        self.assertEqual(Producto, 'Mariana')
        self.assertEqual(categoria, 'García')


if __name__ == '__main__':
    unittest.main()