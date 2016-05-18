names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest_str(list):
	short = list[0]
	for i in list:
		if len(i) < len(short):
			short = i
	return short

print(shortest_str(names))
