# create a function that takes a list and returns a new list that is reversed

numbers = [3, 4, 5, 6, 7]

def reverse_list(input):
    new_list = []
    for i in range(len(input)-1, -1, -1):
        new_list += [input[i]]
    return new_list

print(reverse_list(numbers))
