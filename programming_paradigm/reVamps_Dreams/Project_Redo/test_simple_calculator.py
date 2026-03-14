import unittest
from simple_calculator import SimpleCalculator as c


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.s = c()
    def test_add(self):
        self.assertEqual(self.s.add(5, 10), 15)
        self.assertEqual(self.s.add(-7, 10), 3)
        self.assertEqual(self.s.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(self.s.subtract(5, 10), -5)
        self.assertEqual(self.s.subtract(-7, 10), -17)
        self.assertEqual(self.s.subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(self.s.multiply(5, 10), 50)
        self.assertEqual(self.s.multiply(-7, 10), -70)
        self.assertEqual(self.s.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(self.s.divide(5, 10), 0.5)
        self.assertEqual(self.s.divide(10, 0), None)
        self.assertEqual(self.s.divide(-5, -5), 1)


if __name__ == "__main__":
    unittest.main()