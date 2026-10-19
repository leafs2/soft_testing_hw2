import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(3, 7)
        self.assertEqual(result, 21)

if __name__ == "__main__":
    unittest.main()