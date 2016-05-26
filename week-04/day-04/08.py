# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def remove_x(string):
    if len(string) < 1:
        return string
    elif string[0] == 'x':
        return '' + remove_x(string[1:])
    else:
        return string[0] + remove_x(string[1:])


print(remove_x('xilox'))
