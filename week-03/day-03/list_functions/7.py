# create a function that takes a list and returns a new list with all the elements doubled

def elements_doubled(input):
    list_length = len(input)
    for i in range(list_length):
        input += [input[i]]
    return input

print(elements_doubled([1,2,3]))

def double_value_of_elements(input):
    for i in range(len(input)):
        input[i] *= 2
    return input

print(double_value_of_elements([1,2,3]))
# 
# def double_value_of_elements(input):
#     for i in input:
#         i *= 2
#     return i
#
# print(double_value_of_elements([1,2,3]))
