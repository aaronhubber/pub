import unittest
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):

    def setUp(self):
       self.drink = Drink("Tennants", 3, "beer")
       self.pub = Pub("The Sand Dragoon", self.drink)

    def test_pub_has_name(self):
        self.assertEqual("The Sand Dragoon", self.pub.name)
    
    def test_till_total (self):
        self.assertEqual (100, self.pub.till)

    def test_drink_collection (self):
        self.assertEqual("Tennants", self.drink.name)
