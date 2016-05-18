numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def minimal(list):
	mini = list[0]
	for i in list:
		if i < mini:
			mini = i
	return mini

print(minimal(numbers))
