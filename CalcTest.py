import unittest
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_power_positive_base_and_exponent(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_power_zero_to_zero(self):
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_negative_exponent(self):
        self.assertEqual(self.calc.power(2, -2), 0.25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_negative_operands(self):
        self.assertEqual(self.calc.modulo(-7, 3), 2)
        self.assertEqual(self.calc.modulo(7, -3), -2)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()