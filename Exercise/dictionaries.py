# Nested Dictionaries
cities = {
	'bishkek': {
		'country': 'kyrgyzstan',
		'population': 20000,
		'fact': 'best city'
	},
	'washington': {
		'country': 'united states of america',
		'population': 40000,
		'fact': 'cool city',
	},
	'berlin': {
		'country': 'germany',
		'population': 300000,
		'fact': 'nice city',
	},
}

for city, city_info in cities.items():
	print("\nCity: " + city.title())
	print("\tCountry: " + city_info['country'].title())
	print("\tPopulation: " + str(city_info['population']))
	print("\tAbout City: " + city_info['fact'].title())