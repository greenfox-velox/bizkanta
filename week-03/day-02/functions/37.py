numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def even_nums(list):
	otherlist = []
	for i in range(len(list)):
		if list[i] % 2 == 0:
			otherlist.append(list[i])
	return otherlist

print(even_nums(numbers))

# or

def filter_odds(input):
	evens = []
	for i in input:
		if i % 2 == 0:
			evens += [i]
	return evens

print(filter_odds(numbers))
