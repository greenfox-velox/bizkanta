numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

# def reverse_list(list):
# 	print(list[::-1])
#
# reverse_list(numbers)

def revert(input):
	reverse = []
	for i in range(len(input)-1, -1, -1):
		reverse += [input[i]]
	return reverse

print(revert(numbers))
