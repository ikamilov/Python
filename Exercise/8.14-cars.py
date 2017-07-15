def make_car(manufacturer, model, **car_info):
	info = {}
	info['manufacturer'] = manufacturer
	info['model'] = model
	for key, value in car_info.items():
		info[key] = value
	return info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)