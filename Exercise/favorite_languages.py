from collections import OrderedDict

lists = OrderedDict()

lists['1'] = 'a'
lists['2'] = 'b'

for n, a in lists.items():
	print(n + " " + a)