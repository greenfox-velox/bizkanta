# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name): # file_name -> string
    f = open(file_name, 'r') # f -> file
    result = f.read()
    f.close()
    return result

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    for i in range(number):
        result = f.readline()
    f.close()
    return result.rstrip()

# print(readline('texts/zen_of_python.txt', 6))

# other solution

# def readline(file_name, number):
#     f = open(file_name)
#     result = f.readlines()[number - 1].rstrip()
#     f.close()
#     return result

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    s_without_point = sentence.rstrip('.')
    list1 = s_without_point.split()
    return list1

# print(words('Beautiful is better than ugly.'))

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    sentence = ' '.join(words) + ('.')
    return sentence

# print(sentence(['This', 'is', 'a', 'long', 'sentence']))

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    char_codes = []
    for i in string:
        char_codes += [ord(i)]
    return char_codes

# print(char_codes('almafa'))


# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    str = ''
    for i in char_codes:
        str += chr(i)
    return str

# print(string([97, 108, 109, 97, 102, 97]))
