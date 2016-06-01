# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def num_of_lines(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        num_of_lines = len(lines)
        f.close()
        print(num_of_lines)
    except FileNotFoundError:
        print('0')


num_of_lines('test.txt')
num_of_lines('tests.txt')
