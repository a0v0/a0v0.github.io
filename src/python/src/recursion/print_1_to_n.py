#  Program to print numbers from 1 to n
number = int(input("Enter number: "))


def p(n):
    if n == 0:
        return
    p(n - 1)
    print(n)


p(number)
