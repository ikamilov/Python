def country_name(city, country, population = ''):
	full_name = city.title() + ", " + country.title()
	if population:
		full_name += " - population " + str(population)
	return full_name 