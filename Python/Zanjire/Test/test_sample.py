import unittest
import sys
sys.path.append('../Initial_project')
from  Python.Zanjire.chain import Chain

class TestFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(Chain('Ali')('Safinal')('is')('the')('best.'), 'Ali Safinal is the best.')


if __name__ == '__main__':
    unittest.main()