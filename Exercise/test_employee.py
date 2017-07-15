import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.info = Employee('Azamat', 'Arapov', 32640)
	def test_defualt_raise(self):
		self.assertTrue(self.info)
unittest.main(0)