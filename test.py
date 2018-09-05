#/usr/bin/env python

import unittest

from assignment2 import *

class TestSolution(unittest.TestCase):

    def test_square(self):
        assert square(10) == 100
        assert square(0) == 0
        
    def test_finite_diff(self):
        assert abs(finite_diff(4, 0.1) - 5.0) < 1e-6
    
    def test_well(self):
        assert abs(well(1.2, 5000, 3000) - 427.44) <= 1e-6 
        
if __name__ == '__main__':
    unittest.main()
