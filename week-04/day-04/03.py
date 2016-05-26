# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

# def sum_digits(num):
#     total = 0
#     for i in str(num):
#         total += int(i)
#     return total

# print(sum_digits(2345))


def sum_digits(num):
    if num % 10 < 1:
        return num
    else:
        last_digit = num % 10
        left_digits = num // 10
        return sum_digits(left_digits) + last_digit

print(sum_digits(234))
