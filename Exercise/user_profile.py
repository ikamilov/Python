# Key Arbitrary
def build_profile(first, last, **user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last

	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile0 = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
user_profile1 = build_profile('islam', 'kamilov', location = 'kyrgyzstan', field = 'computer science')
print(user_profile1)