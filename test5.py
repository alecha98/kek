
import unittest
import math

import lib

class LibTest(unittest.TestCase):

    def test_sin_non_negative_arg(self):
        self.assertEqual(lib.sin((math.pi),0))
        self.assertEqual(lib.sin(0), 0 )
        self.assertEqual(lib.sin(math.pi*1,5),-1 )

unittest.main(verbosity=2)