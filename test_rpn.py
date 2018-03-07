import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_factorial(self):
		result = rpn.calculate('4 !')
		self.assertEqual(24, result)
	def test_summation(self):
		result = rpn.calculate('3 5 8 $')
		self.assertEqual(16, result)
	def test_copy(self):
		result = rpn.calculate('2 4 6 * +')
		self.assertEqual(14, result)

