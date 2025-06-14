import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):

        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
        self.assertEqual(self.calc.subtract(5, -6), 11)

    def test_multiply(self):

        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(-2, 7), -14)
        self.assertEqual(self.calc.multiply(-5, -2), 10)

    def test_divide(self):

        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
if __name__ == '__main__':
    unittest.main()
