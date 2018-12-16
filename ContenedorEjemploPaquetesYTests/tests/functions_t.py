import unittest
from package.functions import Operations

class TestPrueba(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_sumatorio(self):
        list = [4,3]
        calc = Operations()
        result = calc.suma(list)
        self.assertEqual(result, 7)

    def test_division(self):
        list = [4,2]
        result = Operations().divide(list)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        list = [2,3]
        result = Operations().multiply(list)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
