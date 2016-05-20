# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']


def is_palindrome(string):
    return string == string[::-1]

def search_palindromes(string):
    palindrome = []
    min_len = 3
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            substring = string[i:j]
            if len(substring) >= min_len:
                if is_palindrome(substring):
                    palindrome += [substring]
    return palindrome

print(is_palindrome('mommy'))
print(is_palindrome('mom'))
print(search_palindromes('mommy'))
print(search_palindromes('dog goat dad duck doodle never'))
