import unittest
from bs4 import BeautifulSoup
import sys
sys.path.append('../Initial_project')
from MainPythonProject.QueraProblemSet.QueraStartDate.chesstml.chesstml import process


class Test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(process("C:\\Users\\p.rezaieh\\PycharmProjects\\MainPythonProject\\QueraProblemSet\\QueraStartDate\\chesstml\\htmlsampletest1.html"), 1)

	def test_2(self):
		self.assertEqual(process("C:\\Users\\p.rezaieh\\PycharmProjects\\MainPythonProject\\QueraProblemSet\\QueraStartDate\\chesstml\\htmlsampletest2.html"), 4)
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									

if __name__ == '__main__':
    unittest.main()