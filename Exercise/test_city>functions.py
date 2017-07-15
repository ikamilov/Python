import unittest
from city_functions import country_name

class TestCities(unittest.TestCase):
	def test_city_function(self):
		full = country_name('santiago', 'chile')
		self.assertEqual(full, 'Santiago, Chile')
	def test_city_population_function(self):
		full = country_name('santiago', 'chile', 600002)
		self.assertEqual(full, "Santiago, Chile - population 600002")
		
unittest.main()