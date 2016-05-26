# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

# def bunny_nums(num):
#     total = 0
#     for i in range(1, num + 1):
#         if i % 2 == 1:
#             total += 2
#         else:
#             total += 3
#     return total
#
# print(bunny_nums(4))

def bunny_ears(n):
    if n <= 0:
        return n
    elif n % 2 == 1:
        return bunny_ears(n - 1) + 2
    else:
        return bunny_ears(n - 1) + 3

print(bunny_ears(5))
