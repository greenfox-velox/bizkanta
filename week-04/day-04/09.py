# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separated_chars_with_stars(string):
    if len(string) < 2:
        return string[0]
    else:
        return string[0] + '*' + separated_chars_with_stars(string[1:])

print(separated_chars_with_stars('table'))
