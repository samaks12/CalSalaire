import unittest
from testSalaire import *


class MyFirstTests(unittest.TestCase):

    def CalculerSalaire1(self):
        self.assertEqual(CalculerSalaire(metier, experience), '4000')

    def CalculerSalaire2(self):
        self.assertEqual(scoreCal(metier, experience), '7000')

    def CalculerSalaire3(self):
        self.assertEqual(scoreCal(metier,experience), '5000')