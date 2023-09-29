# Program to print prime number

num = int(input("Enter a number: "))


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if isPrime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
