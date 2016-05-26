# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

# def change_x_to_y(string):
#     new_string = ''
#     for i in string:
#         if i == 'x':
#             new_string += 'y'
#         else:
#              new_string += i
#     return new_string
#
# print(change_x_to_y('xilox'))

def change_x_to_y(string):
    if len(string) < 1:
        return string
    elif string[0] == 'x':
        return 'y' + change_x_to_y(string[1:])
    else:
        return string[0] + change_x_to_y(string[1:])


print(change_x_to_y('xilox'))
