import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(5, result)

    def test_subtraction(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(2, result)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(6, result)

    def test_division(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(5, result)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
