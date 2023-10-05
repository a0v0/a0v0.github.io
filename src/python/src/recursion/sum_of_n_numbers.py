# Program to print sum of n integers using recursion

z = int(input("Enter number: "))


def s(n):
    if n == 0:
        return 0
    return n + s(n - 1)


print(s(z))
