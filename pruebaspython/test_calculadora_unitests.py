import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(3, 1), 2)

    def test_dividir(self):
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(0, 4), 0)

    def test_exception(self):
        self.assertRaises(ValueError, dividir, 2, 0)


if __name__ == "__main__":
    unittest.main()
