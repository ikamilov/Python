from restaurant import Restaurant, IceCreamStand	

restaurant = IceCreamStand('starbucks', 'coffee')
restaurant.flavor.desribe_flavor()
print(restaurant.desribe_restaurant())
kyrgyz_restaurant = Restaurant('naavat', 'mix')
chinese_restaurant = Restaurant('king palace', 'buffet')
mediteranean_restaurant = Restaurant('dimassis', 'buffet')
print(kyrgyz_restaurant.restaurant_name.title() + " is the best place with " + 
	kyrgyz_restaurant.cuisine_type.title())
kyrgyz_restaurant.desribe_restaurant()
chinese_restaurant.desribe_restaurant()
mediteranean_restaurant.desribe_restaurant()
kyrgyz_restaurant.years_served()
kyrgyz_restaurant.set_number_served(5)
kyrgyz_restaurant.years_served()
kyrgyz_restaurant.increment_number_served(4)
kyrgyz_restaurant.years_served()