# create a function that returns it's input factorial

def factorial(num):
    number = 1
    for i in range(2, num + 1):
        number *= i
    return number

print(factorial(5))
