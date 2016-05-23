# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    reversed_text = ''
    for line in lines:
        reversed_line = line[::-1]
        reversed_line = reversed_line.lstrip()
        reversed_text += reversed_line + "\n"
    f.close()
    return reversed_text

print(decrypt('texts/reversed_zen_lines.txt'))
