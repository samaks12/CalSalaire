import unittest
from CalculSalaire import *

class MyFirstTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(CalculerSalaire('Architecte',4), '4000 euros')


    def test2(self):
        self.assertEqual(CalculerSalaire('médecin',8), '7000 euros')


    def test3(self):
        self.assertEqual(CalculerSalaire('consultant', 5), '5000 euros')


if __name__ == '__main__':
    unittest.main()