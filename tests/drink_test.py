import unittest

from src.drink import *

class TestDrink(unittest.TestCase):


    def setUp(self):
        self.drink = Drink("Tennants", 3, "beer")

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)
    
    def test_drink_price(self):
        self.assertEqual(3, self.drink.price)
    
    def test_drink_type(self):
        self.assertEqual("beer", self.drink.type)