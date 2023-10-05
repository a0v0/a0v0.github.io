# Program to print recursive sum


def rs(a, b):
    if a == 0:
        return b
    return rs(a - 1, b + 1)


print(rs(5, 5))
