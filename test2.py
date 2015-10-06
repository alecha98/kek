
import unittest

import lib

class LibTest(unittest.TestCase):

    def test_even_non_negative_arg(self):
        self.assertEqual(lib.factorial(2),2)
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(0), 0)
        self.assertEqual(lib.factorial(4), 24)

    def test_factorial_negative(self):

        self.assertEqual(lib.factorial(-1), 1)

unittest.main(verbosity=2)