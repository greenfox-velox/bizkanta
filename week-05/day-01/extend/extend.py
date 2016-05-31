
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param

def median(pool):
    lst = sorted(pool)
    if len(lst) < 1:
        return None
    if len(lst) % 2 == 1:
        return lst[int((len(lst)-1)/2)]
    else:
        return (lst[int((len(lst)/2)-1)] + lst[int(len(lst)/2)])/2

# Returns true if the param is a vovel
def is_vovel(char):
    if char.lower() in 'aeiou':
        return True
    else:
        return False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    new_string = ''
    for char in teve:
        if is_vovel(char):
            new_string += (char+'v'+char)
        else:
            new_string += char
    return new_string

# print(translate('alma'))
