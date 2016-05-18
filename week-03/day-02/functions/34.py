numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def total(nums):
	summa = 0
	for i in nums:
		summa += i
	return summa

print(total(numbers))
