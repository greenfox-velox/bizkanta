# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    lines_list = f.readlines()
    reversed_lines_list = lines_list[::-1]
    reversed_text = ''.join(reversed_lines_list)
    f.close()
    return reversed_text

print(decrypt('texts/reversed_zen_order.txt'))
