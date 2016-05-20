# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']


def search_palindromes(string):
    palindrome = []
    for i in range(len(string) - 2):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindrome += [substring]
    return palindrome

print(search_palindromes('retipipiter'))
print(search_palindromes('dog goat dad duck doodle never'))
