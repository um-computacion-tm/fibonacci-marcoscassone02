import unittest
from fibonacci import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    def test_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
    def test_10(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34)
if __name__ == '__main__':
    unittest.main()