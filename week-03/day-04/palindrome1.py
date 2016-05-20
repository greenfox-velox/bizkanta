# Create a function that takes a string and creates a palindrome from it. It should work like this:
#
# output = create_palindrome('pear')
#
# print(output) # it prints: pearraep

def create_string_and_palindrome(string):
    return string + string[::-1]

print(create_string_and_palindrome('palindrome'))
