import unittest
from src.pub import *

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Sand Dragoon", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Sand Dragoon", self.pub.name)