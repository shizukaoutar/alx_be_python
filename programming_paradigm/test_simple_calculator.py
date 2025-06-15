from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCaculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        """Test subtraction method"""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
    def test_multiplication(self):
        """Test multiplication method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
    def test_division(self):
        """Test division method"""
        self.assertEqual(self.calc.divide(14, 2), 7)
        self.assertEqual(self.calc.divide(14, 0), None)



