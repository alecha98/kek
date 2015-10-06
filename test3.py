
import unittest

import lib

class LibTest(unittest.TestCase):

    def test_even_non_negative_arg(self):
        self.assertEqual(lib.even['haah'], True)
        self.assertEqual(lib.even['aaah'], False)
        self.assertEqual(lib.even['beneb'], True)

unittest.main(verbosity=2)