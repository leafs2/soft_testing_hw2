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

    # -------------------------------------------------------------
    # Question 7: Metamorphic / Property-Based Tests
    # -------------------------------------------------------------
    def test_metamorphic_addition_subtraction_inverse(self):
        """Metamorphic relation: subtract(add(a, b), b) == a"""
        test_pairs = [(42, 17), (-15, 8), (1000, -250), (0, 99)]
        for a, b in test_pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(self.calc.add(a, b), b), a)

    def test_metamorphic_addition_commutativity(self):
        """Metamorphic relation: add(a, b) == add(b, a)"""
        test_pairs = [(13, 29), (-50, 50), (12345, 67890)]
        for a, b in test_pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    def test_metamorphic_multiplication_division_inverse(self):
        """Metamorphic relation: divide(multiply(a, b), b) == a (for b != 0)"""
        test_pairs = [(10, 2), (-30, 5), (100, 4)]
        for a, b in test_pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(self.calc.multiply(a, b), b), a)

if __name__ == "__main__":
    unittest.main()