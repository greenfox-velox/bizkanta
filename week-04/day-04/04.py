# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

# def squared(n, power):
#     return n ** power

# print(squared(4,3))

def squared(n, power):
    if power <= 1:
        return n
    else:
        return squared(n, power-1) * n

print(squared(4,3))
