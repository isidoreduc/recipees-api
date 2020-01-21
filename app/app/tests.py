from django.test import TestCase
from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add(self):
        """Test corect function of addition"""
        self.assertEqual(add(8,7),15)

    def test_subtract(self):
        """Test correct subtraction"""
        self.assertEqual(subtract(13,8),5)
