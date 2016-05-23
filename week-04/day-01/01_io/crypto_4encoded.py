# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    file = open(file_name)
    lines = file.readlines()
    new_text = ''
    for line in lines:
        for char in line:
            if char == ' ' or char == '\n':
                new_text += char
            else:
                char_code = ord(char)
                prev_char_code = char_code - 1
                prev_char = chr(prev_char_code)
                new_text += prev_char
    file.close()
    return new_text

print(decrypt('texts/encoded_zen_lines.txt'))

# Create a method that decrypts texts/encoded_zen_lines.txt
# def decrypt(file_name):
#     file = open(file_name)
#     lines = file.readlines()
#     new_text = ''
#     for line in lines:
#         for char in line:
#             if char != ' ' and char != '\n':
#                 char_code = ord(char)
#                 char_code -= 1
#                 char = chr(char_code)
#             new_text += char
#     file.close()
#     return new_text
#
# print(decrypt('texts/encoded_zen_lines.txt'))
