import unittest
from Boa_Constrictor import Boa_Constrictor
from Huron import Huron

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        # Configuración de la instancia de Boa_Constrictor para las pruebas
        self.boa = Boa_Constrictor("Boa", 5, 30.0, "Brasil", 0.3)

    def test_comer_ratones(self):
        # Alimenta a la boa hasta alcanzar el límite de 10 ratones
        for _ in range(10):
            self.boa.comer_ratones()

        # Verifica que se lance un ValueError en el intento 11 de alimentar con ratones
        with self.assertRaises(ValueError) as context:
            self.boa.comer_ratones()

        # Comprueba que el mensaje de la excepción sea "Demasiados Ratones!"
        self.assertEqual(str(context.exception), "Demasiados Ratones!")



class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Hurón", 2, 5.0, "España", 0.2)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        # El cálculo debería ser peso * impuestos
        self.assertAlmostEqual(self.huron.calcular_flete(), 5.0 * 0.2)


if __name__ == "__main__":
    unittest.main()
