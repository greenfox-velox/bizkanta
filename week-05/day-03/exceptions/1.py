# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_with_ten(number):
    try:
        print(10 / number)
    except ZeroDivisionError:
        print('fail')

divide_with_ten(10)
divide_with_ten(0)
