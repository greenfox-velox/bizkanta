# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

# def bunny_ears(n):
#     total = 0
#     for i in range(n + 1):
#         total += i
#     return total * 2
#
# print(bunny_ears(3))

def bunny_ears(n):
    if n <= 0:
        return n
    else:
        return bunny_ears(n - 1) + 2

print(bunny_ears(3))
