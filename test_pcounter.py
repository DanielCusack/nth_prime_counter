#!/usr/bin/env python3
import unittest
from pcounter import *

class Test_pcounter(unittest.TestCase):
    def test_pcounter(self):
        #Test that first six primes are found
        self.assertEqual(Prime_Finder(1).num, 2)
        self.assertEqual(Prime_Finder(2).num, 3)
        self.assertEqual(Prime_Finder(3).num, 5)
        self.assertEqual(Prime_Finder(4).num, 7)
        self.assertEqual(Prime_Finder(5).num, 11)
        #Test a large number prime
        self.assertEqual(Prime_Finder(10000).num, 104729)


if __name__ == '__main__':
    unittest.main()