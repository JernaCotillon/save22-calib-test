import calculator2
import unittest


class TestCalculator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator2.add(1,1),2)
	
		with self.assertRaises(TypoError):
			calculator2.add('1',1)


	def test_sub(self):
		self.assertEqual(calculator2.sub(1,1),0)

	def test_mul(self):
		self.assertEqual(calculator2.mul(1,1),1)

	def test_div(self):
		self.assertEqual(calculator2.div(1,1),1)
		with self.assertRaises(ZeroDivisionError):
			calculator2.div(10,0)


if __name__ == "__main__":
	unittest.main()
