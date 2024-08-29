"""
Sample Tests
"""

from django.test import SimpleTestCase
import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """Test adding the numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test Subtracting the numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
