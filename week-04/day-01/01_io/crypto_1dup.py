# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    lines = f.readlines()
    new_text = ''
    for line in lines:
        for i in range(0, len(line), 2):
            new_text += line[i]
    f.close()
    return new_text

print(decrypt('texts/duplicated_chars.txt'))
