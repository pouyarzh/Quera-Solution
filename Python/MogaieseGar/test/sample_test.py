import unittest
import sys
import pytest
sys.path.append('../Initial_project')
from MainPythonProject.QueraProblemSet.QueraStartDate.MogaieseGar import moghayeseGar


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual('las', moghayeseGar.compare('ali', 'salib'))

	def test_2(self):
		self.assertEqual('Both strings are empty!', moghayeseGar.compare('nima', 'amin'))


if __name__ == '__main__':
    unittest.main()