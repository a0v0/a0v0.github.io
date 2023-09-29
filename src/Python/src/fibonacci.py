# print fibonacci upto a given n numbers


def fib(n):
    first = 0
    second = 1

    if n == 1:
        print(first)
    elif n == 2:
        print(first, second)
    else:
        print(first, second, end=" ")
        for i in range(n - 2):
            third = first + second
            first = second
            second = third
            print(second, end=" ")


fib(int(input("Enter a number: ")))
