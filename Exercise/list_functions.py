# Functions
def make_album(name, title, tracks = '1'):
	collection = {'name': name, 'title': title}
	if tracks:
		collection['tracks'] = tracks 
	return collection

while True:
	print("\nPlease Enter 'q' to quit")
	a_name = input("Enter Artist Name: ")
	if a_name == 'q':
		break
	a_title = input("Enter Title: ")
	if a_title == 'q':
		break
	a_tracks = input("Enter tracks: ")
	if a_tracks == 'q':
		break
	artist = make_album(a_name, a_title, a_tracks)
	print(artist)


