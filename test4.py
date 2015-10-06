
import unittest

import lib

class LibTest(unittest.TestCase):

    def test_prime_non_negative_arg(self):
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(-2), False)
        self.assertEqual(lib.prime(1), True)
        self.assertEqual(lib.prime(0), False)

unittest.main(verbosity=2)