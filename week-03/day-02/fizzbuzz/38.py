# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# for i in range(1, 101):
# 	if i % 3 == 0 and i % 5 == 0:
# 		print("FizzBuzz")
# 	elif i % 3 == 0:
# 		print("Fizz")
# 	elif i % 5 == 0:
# 		print("Buzz")
# 	else:
# 		print(i)

#
# for i in range(1, 101):
# 	printable = i
# 	if i % 3 == 0 and i % 5 == 0:
# 		printable = "FizzBuzz"
# 	elif i % 3 == 0:
# 		printable = "Fizz"
# 	elif i % 5 == 0:
# 		printable ="Buzz"
# 	print(printable)


for i in range(1, 101):
    printable = ""
    if i % 3 == 0:
		printable += "Fizz"
	if i % 5 == 0:
		printable += "Buzz"
	if printable == "":
		printable = i
	print(printable)


# with while
# i = 1;
#
# while i <= 100:
# 	if i % 3 == 0 and i % 5 == 0:
# 		print("FizzBuzz")
# 	elif i % 3 == 0:
# 		print("Fizz")
# 	elif i % 5 == 0:
# 		print("Buzz")
# 	else:
# 		print(i)
# 	i += 1