# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

# def count_down(n):
#     for i in range(n, 0, -1):
#         print(i)

# def count_down(n):
#     if n <= 0:
#         pass
#     else:
#         print(n)
#         count_down(n-1)
#
# print(count_down(10))


def concat(n):
    if n <= 0:
        return []
    else:
        return concat(n - 1) + [n]

print(concat(10))
